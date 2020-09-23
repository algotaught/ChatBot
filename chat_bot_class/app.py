from flask import Flask, render_template, request, jsonify
from flask_cors import CORS, cross_origin
import requests
import bs4
import os
from flask import make_response
import json
from city_data import city_finder


app= Flask(__name__)

@app.route('/webhook', methods=['POST'])
@cross_origin()
def webhook():
    req=request.get_json(silent=True, force=True)
    print(req)
    intent=req.get('queryResult').get('intent').get('displayName')
    if intent== 'population':
        print(req)
        cityName= req.get('queryResult').get('parameters').get('geo-city')
        res= city_finder(cityName)
        print(res)
        return res
    else:
        return {'fulfillmentText':'intent not matching'}

if __name__=='__main__':
    app.run(debug=True)