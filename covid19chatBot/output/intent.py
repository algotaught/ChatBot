from flask import Flask, render_template, request, jsonify
from flask_cors import CORS, cross_origin
import requests
import bs4
import os
from flask import make_response
import json
import bs4
from bs4 import BeautifulSoup
import requests
from flask import Flask, render_template, request, jsonify
from cases import count_cases
import guidlines
from guidlines import domesticGuidelines
from helplineNumber import helpLineNumber
class get_facts:
    def __init__(self):
        pass
    def intent_matcher(self,req):
        self.req=req
        sessionID= self.req.get('responseID')
        result = self.req.get("queryResult")
        intent = result.get("intent").get('displayName')
        if intent=='cases':
            x=count_cases()
            cases=x.get_numbers(self.req)
            return cases
        if intent=='domestic travel':
            x=domesticGuidelines()
            guidLines=x.domestic_guidelines()
            return guidLines
        if intent =='help line number':
            number=helpLineNumber()
            num=number.get_help_numbers(self.req)
            return num




