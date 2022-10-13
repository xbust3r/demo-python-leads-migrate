from chalice import Chalice

from chalicelib.infraestructure.adapter.sql.sqlalchemy import SqlAlchemyAdapter
from chalicelib.infraestructure.repository.sqlalchemy.mapping import load_mapper
from chalicelib.infraestructure.repository.sqlalchemy.facebook_leads import FacebookLeadsGatewaySqlAlchemyRepository
from chalicelib.infraestructure.repository.sqlalchemy.conf_ads import ConfAdsGatewaySqlAlchemyRepository

from chalicelib.application.services.routing import routing

import json
import requests
import logging

app = Chalice(app_name='facebook_leads')
app.log.setLevel(logging.DEBUG)


@app.route('/')
def index():
    return {'hello': 'world'}


@app.route('/start/{idlead}', methods=['POST'])
def start(idlead):
    load_mapper()
    request = app.current_request
    data = request.json_body
    #start CLASS
    class_routing = routing(idlead)

    #get lead facebook data
    lead_data = class_routing.get_lead()
    if not lead_data["status"]:
        return json_response(None, "Your ID Lead is incorrect")
    #configure the type of routing, if insurance lead, recruit lead or general lead
    find = class_routing.find_configuration()
    if not find["status"]:
        return json_response(None, "An error has been ocurred while configuring your routing")
    #build the data structure
    validate_routing = class_routing.generate()
    if not validate_routing["status"]:
        return json_response(None, "An error has been ocurred while generate your data")
    #Send Data to custom system
    send_routing = class_routing.send()

    if not send_routing["status"]:
        return json_response(None, "Your lead can't been delivered", send_routing["message"])
    else:
        return json_response(True, "Your lead has been delivered",send_routing["message"])




def json_response(status, message=None, data=None):
    # if (status==None):
    response = {}
    response["status"] = status
    if (message):
        response["message"] = message
    if (data):
        response["data"] = data
    return json.dumps(response)

