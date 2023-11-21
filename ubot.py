import aiohttp
import asyncio
from aiohttp import ClientSession
from aiohttp.client_exceptions import ClientError
from bs4 import BeautifulSoup
from functools import lru_cache
from flask import Flask, jsonify, render_template_string
from aiocache import Cache
from aiocache.serializers import JsonSerializer
import json
import yaml
import csv

app = Flask(__name__)
cache = Cache(Cache.MEMORY, serializer=JsonSerializer(), namespace="coupons", ttl=600)

async def fetch(url):
    async with ClientSession() as session:
        try:
            async with session.get(url) as response:
                return await response.text()
        except ClientError as e:
            print(f"Error fetching URL {url}: {e}")
            return None

@lru_cache(maxsize=None, typed=False)
async def fetch_and_cache(url):
    html = await fetch(url)
    return html

async def fetch_go_link(link):
    html = await fetch_and_cache(link)
    if html:
        soup = BeautifulSoup(html, 'html.parser')
        link_class = soup.select('.ui.center.aligned.basic.segment a')
        return link_class[0].get('href') if link_class else None
    return None

async def fetch_coupon(link):
    html = await fetch_and_cache(link)
    if html:
        soup = BeautifulSoup(html, 'html.parser')
        title = soup.select_one('.ui.grey.header')
        enroll = soup.select_one('.ui.segment a')
        return {'title': title.text.strip(), 'enroll': enroll.get('href')} if title and enroll else None
    return None

async def fetch_coupons():
    try:
        response = await fetch('https://www.discudemy.com/all')
        soup = BeautifulSoup(response, 'html.parser')
        link_class = soup.select('.card-header')
        hn = [item.get('href') for item in link_class]

        go_links = await asyncio.gather(*(fetch_go_link(link) for link in hn))
        coupons = await asyncio.gather(*(fetch_coupon(link) for link in go_links if link))

        valid_coupons = [coupon for coupon in coupons if coupon]

        return valid_coupons
    except Exception as error:
        raise error

async def fetch_and_cache_coupons():
    courses = await fetch_coupons()
    await cache.set("courses", courses)
    return courses

@app.route('/')
async def view_coupons():
    try:
        courses = await cache.get("courses")
        if not courses:
            courses = await fetch_and_cache_coupons()
        html_string = '''
            <!DOCTYPE html>
            <html lang="en">
            <head>
                <meta charset="UTF-8">
                <meta name="viewport" content="width=device-width, initial-scale=1.0">
                <title>FreeEduFetch</title>
                <style>
                    body {
                        font-family: 'Arial', sans-serif;
                        background-image: url('https://i.postimg.cc/ry3pMvBQ/newimg.jpg');
                        background-size: cover;
                        background-repeat: no-repeat !important;
                        margin: 0;
                        padding: 20px;
                    }
                    .container {
                        display: flex;
                        flex-wrap: wrap;
                        gap: 20px;
                        justify-content: space-between;  /* Added for three cards in one line */
                        max-width: 1200px;
                        margin: 0 auto;
                    }
                    .card {
                        flex: 0 0 calc(33.333% - 20px);
                        background-color: rgba(196, 239, 239, 0.55);
                        border: 1px rgba(21, 153, 144, 0.47);
                        border-radius: 8px;
                        overflow: hidden;
                        box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
                        transition: transform 0.2s ease-in-out;
                        margin-bottom: 20px;  /* Added for spacing between rows */
                    }
                    .card:hover {
                        transform: scale(1.05);
                    }
                    .content {
                        padding: 15px;
                        text-align: center;
                    }
                    h3 {
                        margin-top: 0;
                        font-size: 18px;
                        color: #333;
                    }
                    a {
                        display: block;
                        margin-top: 15px;
                        text-decoration: none;
                        background-color: rgba(148, 233, 59, 0.55);
                        color: white;
                        padding: 10px 15px;
                        font-size: 16px;
                        border-radius: 4px;
                        transition: background-color 0.3s ease-in-out;
                    }
                    a:hover {
                        background-color: rgba(119, 189, 46, 0.94);
                    }
               @media screen and (max-width: 767px) {
    .card {
        flex: 0 0 calc(50% - 20px); /* Two cards in a row for screens up to 767px width */
    }
}

@media screen and (max-width: 480px) {
    .card {
        flex: 0 0 calc(100% - 20px); /* One card in a row for screens up to 480px width */
    }
}
 .container {
                        display: flex;
                        flex-wrap: wrap;
                        gap: 20px;
                        justify-content: space-between;  /* Added for three cards in one line */
                        max-width: 1200px;
                        margin: 0 auto;
                    }
.card:hover {
    transform: scale(1.05);
}

.content {
    padding: 15px;
    text-align: center;
}

h3 {
    margin-top: 0;
    font-size: 18px;
    color: #333;
}

a {
    display: block;
    margin-top: 15px;
    text-decoration: none;
    background-color: rgba(148, 233, 59, 0.55);
    color: white;
    padding: 10px 15px;
    font-size: 16px;
    border-radius: 4px;
    transition: background-color 0.3s ease-in-out;
}

a:hover {
    background-color: rgba(119, 189, 46, 0.94);
}
                </style>
            </head>
            <body>
                <div class="container">
        '''

        for course in courses:
            html_string += f'''
                <div class="card">
                    <div class="content">
                        <h3>{course['title']}</h3>
                        <a href="{course['enroll']}" target="_blank">Enroll Now</a>
                    </div>
                </div>
            '''

        html_string += '''
                </div>
            </body>
            </html>
        '''

        return html_string

    except Exception as error:
        print('An error occurred while fetching coupons:', error)
        return jsonify({'error': 'An error occurred while fetching coupons.'}), 500
    
@app.route('/api/coupons/<format>', methods=['GET'])
async def get_coupons_by_format(format):
    try:
        courses = await cache.get("courses")
        if not courses:
            courses = await fetch_and_cache_coupons()

        format_handlers = {
            'json': jsonify,
            'txt': lambda x: jsonify(x),
            'xml': to_xml,
            'yaml': to_yaml,
            'csv': to_csv,
        }

        if format not in format_handlers:
            return jsonify({'error': f'Unsupported format: {format}'}), 400

        return format_handlers[format](courses)

    except Exception as error:
        print('An error occurred while fetching coupons:', error)
        return jsonify({'error': 'An error occurred while fetching coupons.'}), 500

def to_xml(courses):
    xml_data = '<root>\n'
    for index, course in enumerate(courses, start=1):
        xml_data += f'  <item>\n    <index>{index}</index>\n    <title>{course["title"]}</title>\n    <url>{course["enroll"]}</url>\n  </item>\n'
    xml_data += '</root>'
    return xml_data

def to_yaml(courses):
    yaml_data = [{'title': course['title'], 'url': course['enroll']} for course in courses]
    return yaml.dump(yaml_data, default_flow_style=False)

def to_csv(courses):
    csv_data = [['index', 'title', 'url']]
    csv_data.extend([(str(index), course['title'], course['enroll']) for index, course in enumerate(courses, start=1)])
    return csv_data

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001, debug=True)
