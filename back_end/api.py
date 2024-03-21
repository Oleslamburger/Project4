from flask_cors import CORS
import pandas as pd
import os
from flask import Flask, jsonify
import json 


# Flask Setup: Initialize the Flask app.
app = Flask(__name__)
CORS(app, resources={r"/api/*": {"origins": "http://localhost:5000"}})
df_city = pd.read_csv('../location_housing_city.csv')
df_state =pd.read_csv('../location_housing_state.csv')

with open('../us_state_prices.geojson', 'r') as file:
    geojson_data = json.load(file)


#define destination api.
@app.route("/api/v1.0/state")
def state():
    data_dic = [{'state':x["state"],'price':x['price'], 'lat': x["lat"], 'lon': x['lon']} for _,x in df_state.iterrows()]
    return jsonify(data_dic)



#define destination api.
@app.route("/api/v1.0/city")
def city():
    data_dic = [{'city':x["city"] ,'price':x['price'], 'lat': x["lat"], 'lon': x['lon']} for _,x in df_city.iterrows()]
    return jsonify(data_dic)


#define destination api.
@app.route("/api/v1.0/state_geojson")
def state_geojson():

    return jsonify(geojson_data)


if __name__ == '__main__':
    app.run(debug=True)


