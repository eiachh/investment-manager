from glob import glob
import json
import math
from common_lib.const import constants
from flask import Flask,request

class investmentManager():
    def __init__(self):
        self.request_data = ''


    def getPreferredInvestmentJson(self):
        nextInvestment = self.getManagerOptions()
        return nextInvestment


    def getManagerOptions(self):
        researchManagerOption = self.request_data['researchManager']    
        buildingManagerOption = self.request_data['buildingManager']
        #progressionManagerOption = self.request_data['progressionManager']
        finalOption = self.getBestInvestment(researchManagerOption,buildingManagerOption)
        return finalOption
    
        
    def getBestInvestment(self, research, building):
        # Apes together strong
        if self.isResearchable(research):
            return research
        elif self.isConstructable(building):
            return building
       # elif self.isProgressive(progression):
       #    return progression
        else: 
            return {'Result':'None'}
        


    def isResearchable(self, research):
        return (research['researchable']['researchID'] != -1)
            
    def isConstructable(self, building):
        return (building['constructable']['buildingID'] != -1)

    #def isProgressive(self, progression):                     
    #    progBuilding = progression['constructable']
    #    progResearch = progression['researchable']
        #if (progBuilding['buildingID'] != -1 and self.isReasonable(progBuilding['buildingId'], progBuilding['buildingLevel'])):



    #def isReasonable(self, ogameID, ogameLvl):
        

            

investManager = investmentManager()

port = 5004
app = Flask(__name__)

@app.route('/get_investment', methods=['GET'])
def getInvestmentEndpoint(): 
    investManager.request_data = request.get_json()
    respData = investManager.getPreferredInvestmentJson()
    return respData


@app.route('/ready', methods=['GET'])
def getInvestmentReadiness():
    return "{Status: OK}"


app.run(host='0.0.0.0', port = port)
