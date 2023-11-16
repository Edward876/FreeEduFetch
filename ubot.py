from pack import functions
from pack import banner
import json
import os
from flask import Flask, jsonify
from flask_cors import CORS

# A function to create a json out of datas
# def toJson(a):
#     json_list = []
#     for element in a:
#         title, url = element.split("||")
#         json_list.append({"title": title, "url": url})

#     json_file_path = "./output.json"
#     try:
#      json_file = open("./output.json", "w", encoding="utf-8")
#      json.dump(json_list, json_file)
#      print(f"JSON data has been saved to {json_file_path}")
#     except Exception as e:
#      print(f"An error occurred: {e}")
#     print(json_list)

# List returning functions

def discudemy():
    list_of_coupons_and_title = functions.discudemy(1)
    # write_coupons(list_of_coupons_and_title)
    return list_of_coupons_and_title

    

def learnviral():
    list_of_coupons_and_title = functions.learnviral(1)
    # write_coupons(list_of_coupons_and_title)
    return list_of_coupons_and_title

def real_disc():
    list_of_coupons_and_title = functions.real_disc(1)
    # write_coupons(list_of_coupons_and_title)
    return list_of_coupons_and_title

def udemy_freebies():
    list_of_coupons_and_title = functions.udemy_freebies(1)
    # write_coupons(list_of_coupons_and_title)
    return list_of_coupons_and_title

def udemy_coupons_me():
    list_of_coupons_and_title = functions.udemy_coupons_me(1)
    # write_coupons(list_of_coupons_and_title)
    return list_of_coupons_and_title    

# combined_list = [item for sublist in [discudemy(), real_disc(), udemy_freebies(), udemy_coupons_me()] if sublist for item in sublist]



#using Flask
app = Flask(__name__)
@app.route('/api/coupons', methods=['GET'])
def get_coupons():
    combined_list = [item for sublist in [discudemy(), real_disc(), udemy_freebies(), udemy_coupons_me()] if sublist for item in sublist]
    json_data = toJson(combined_list)
    return jsonify(json_data)
CORS(app)

def toJson(a):
    json_list = []
    for element in a:
        title, url = element.split("||")
        json_list.append({"title": title, "url": url})
    return json_list

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=int(os.environ.get('PORT', 5000)))
  
