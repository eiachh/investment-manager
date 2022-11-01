from glob import glob
import json
import math
from common_lib.const import constants
from flask import Flask,request

class investmentManager():
    def __init__(self):
        self.request_data = ''

    def getPreferredInvestmentJson(self):
        return {'Result': 'None'}


investManager = investmentManager()

port = 5004
app = Flask(__name__)

@app.route('/get_investment', methods=['GET'])
def getInvestmentEndpoint(): 
    investManager.request_data = request.get_json()
    


@app.route('/ready', methods=['GET'])
def getInvestmentReadiness():
    return "{Status: OK}"


app.run(host='0.0.0.0', port = port)
