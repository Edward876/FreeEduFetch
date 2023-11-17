from pack import functions
import json
import os
from flask import Flask, jsonify, make_response
from dicttoxml import dicttoxml
import yaml
import csv
from io import StringIO
from flask_cors import CORS
app = Flask(__name__)


def discudemy():
    list_of_coupons_and_title = functions.discudemy(1)
    return list_of_coupons_and_title

def learnviral():
    list_of_coupons_and_title = functions.learnviral(1)
    return list_of_coupons_and_title

def real_disc():
    list_of_coupons_and_title = functions.real_disc(1)
    return list_of_coupons_and_title

def udemy_freebies():
    list_of_coupons_and_title = functions.udemy_freebies(1)
    return list_of_coupons_and_title

def udemy_coupons_me():
    list_of_coupons_and_title = functions.udemy_coupons_me(1)
    return list_of_coupons_and_title    




def toJson(a):
    json_list = []
    for element in a:
        title, url = element.split("||")
        json_list.append({"title": title, "url": url})
    return json_list

def toTxt(a):
    txt_list = []
    txt_list.append("FREE EDU FETCH\n")
    for index, element in enumerate(a, start=1):
        title, url = element.split("||")
        txt_list.append(f"{index}. {title}\n   {url}\n")
    return ''.join(txt_list)

def toXml(a):
    xml_data = '<root>\n'
    for index, element in enumerate(a, start=1):
        title, url = element.split("||")
        xml_data += f'  <item>\n    <index>{index}</index>\n    <title>{title}</title>\n    <url>{url}</url>\n  </item>\n'
    xml_data += '</root>'
    return xml_data

def toYaml(a):
    yaml_data = [{'title': title, 'url': url} for title, url in [element.split("||") for element in a]]
    return yaml.dump(yaml_data, default_flow_style=False)

def toCsv(a):
    csv_data = [['index', 'title', 'url']]
    csv_data.extend([(str(index), title, url) for index, (title, url) in enumerate([element.split("||") for element in a], start=1)])
    return csv_data

#using Flask
@app.route('/api/coupons/json', methods=['GET'])
def get_coupons_json():
    combined_list = [item for sublist in [discudemy(), real_disc(), udemy_freebies(), udemy_coupons_me()] if sublist for item in sublist]
    json_data = toJson(combined_list)
    return jsonify(json_data)

@app.route('/api/coupons/txt', methods=['GET'])
def get_coupons_txt():
    combined_list = [item for sublist in [discudemy(), real_disc(), udemy_freebies(), udemy_coupons_me()] if sublist for item in sublist]
    txt_data = toTxt(combined_list)
    return txt_data, 200, {'Content-Type': 'text/plain'}

@app.route('/api/coupons/xml', methods=['GET'])
def get_coupons_xml():
    combined_list = [item for sublist in [discudemy(), real_disc(), udemy_freebies(), udemy_coupons_me()] if sublist for item in sublist]
    xml_data = toXml(combined_list)
    response = make_response(xml_data)
    response.headers['Content-Type'] = 'application/xml'
    return response

@app.route('/api/coupons/yaml', methods=['GET'])
def get_coupons_yaml():
    combined_list = [item for sublist in [discudemy(), real_disc(), udemy_freebies(), udemy_coupons_me()] if sublist for item in sublist]
    yaml_data = toYaml(combined_list)
    response = make_response(yaml_data)
    response.headers['Content-Type'] = 'application/yaml'
    return response

@app.route('/api/coupons/csv', methods=['GET'])
def get_coupons_csv():
    combined_list = [item for sublist in [discudemy(), real_disc(), udemy_freebies(), udemy_coupons_me()] if sublist for item in sublist]
    csv_data = toCsv(combined_list)

    # Create a file-like object in memory
    csv_buffer = StringIO()
    writer = csv.writer(csv_buffer)

    # Write CSV data to the buffer
    writer.writerows(csv_data)

    response = make_response(csv_buffer.getvalue())
    response.headers['Content-Type'] = 'text/csv'
    response.headers['Content-Disposition'] = 'attachment; filename=coupons.csv'

    return response

CORS(app)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001, debug=False)
  
