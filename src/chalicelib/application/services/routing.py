from chalicelib.application.services.lead import lead
from chalicelib.application.services.configuration import configuration

import json
import logging
import requests
import os

class routing:
    lead_id = None
    routing = None
    routing_data = {}
    lead_data = {}
    lead_obj = None

    type = None
    ad_id = None
    adset_id = None
    campaign_id = None
    fanpage_id = None

    routing_type = None
    routing_media_code = None
    routing_code = None
    routing_slug = None

    data_json = {}

    _lead = None
    _configuration = None

    def __init__(self, lead_id):
        self.lead_id = lead_id
        self._lead = lead()
        self._configuration = configuration()

    def generate(self):
        status = dict()

        if self.routing_type == "recruit":
            self.generate_zatanna()
            self.data_zatanna()
            self.routing_slug = "/recruit/confie-mx/save/v1"
            status["status"] = True
        if self.routing_type == "franchise":
            self.generate_zatanna()
            self.data_zatanna()
            status["status"] = True
        if self.routing_type == "insurance":
            self.generate_insurance()
            self.data_insurance()
            status["status"] = True

        if not status["status"]:
            status["status"] = None

        logging.info(status["status"])
        return status

    def generate_zatanna(self):
        self.data_json["code"] = self.routing_code
        self.data_json['content'] = {}
        self.data_json["content"]["media_code"] = self.routing_media_code

    def data_zatanna(self):

        self.data_json['content']['recaptcha_response'] = 'asdfzxc666789'
        self.data_json['content']['recaptcha_response_score'] = 2;
        self.data_json['content']['email'] = self.lead_data["email"]
        self.data_json['content']['phone'] = self.lead_data["phone_number"]
        self.data_json['content']['first_name'] = self.lead_data["first_name"]
        self.data_json['content']['last_name'] = self.lead_data["last_name"]
        self.data_json['content']['zip_code'] = self.lead_data["zip_code"]
        self.data_json['content']['source_system'] = "facebook Ads Microservice Zatanna"

    def generate_insurance(self):
        self.data_json['lead'] = {}
        self.data_json["lead"]["media_code"] = self.routing_media_code

    def data_insurance(self):

        self.data_json['lead']['email'] = self.lead_data["email"]
        self.data_json['lead']['phone'] = self.lead_data["phone_number"]
        self.data_json['lead']['first_name'] = self.lead_data["first_name"]
        self.data_json['lead']['last_name'] = self.lead_data["last_name"]
        self.data_json['lead']['zipcode'] = self.lead_data["zip_code"]
        self.data_json['lead']['source_system'] = "facebook Ads Microservice Insurance"
        self.data_json['lead']['communications_consent'] = "4a"

    def get_lead(self):
        id = self.lead_id
        self.lead_obj = self._lead.get_lead(id)
        if not self.lead_obj:
            return {"status": None}
        else:
            self.lead_data["first_name"] = self.lead_obj.first_name
            self.lead_data["last_name"] = self.lead_obj.last_name
            self.lead_data["phone_number"] = self.lead_obj.phone_number
            self.lead_data["zip_code"] = self.lead_obj.zip_code
            self.lead_data["email"] = self.lead_obj.email

            self.ad_id = self.lead_obj.ad_id
            return {"status": True}

    def find_configuration(self):
        conf_ad = self._configuration.find_ad(self.ad_id)
        if conf_ad:
            self.routing_type = conf_ad.type
            self.routing_media_code = conf_ad.media_code
            self.routing_code = conf_ad.code
            self.type = "ad"
            return {"status": True}
        if self.lead_obj.ads.adsets.ad_set_id:
            self.adset_id = self.lead_obj.ads.adsets.ad_set_id
            logging.info(self.adset_id)
            conf_adset = self._configuration.find_adset(self.adset_id)
            if conf_adset:
                self.routing_type = conf_adset.type
                self.routing_media_code = conf_adset.media_code
                self.routing_code = conf_adset.code
                self.type = "adset"
                return {"status": True}
        #self.campaign_id = 5
        if self.lead_obj.ads.adsets.campaigns.campaign_id:
            self.campaign_id = self.lead_obj.ads.adsets.campaigns.campaign_id
            logging.info(self.campaign_id)
            conf_campaign = self._configuration.find_campaign(self.campaign_id)
            if conf_campaign:
                self.routing_type = conf_campaign.type
                self.routing_media_code = conf_campaign.media_code
                self.routing_code = conf_campaign.code
                self.type = "campaign"
                return {"status": True}
        if self.lead_obj.ads.adsets.campaigns.brands.fanpage_id:
            self.fanpage_id = self.lead_obj.ads.adsets.campaigns.brands.fanpage_id
            logging.info(self.fanpage_id)
            conf_fanpage = self._configuration.find_fanpage(self.fanpage_id)
            if conf_fanpage:
                self.routing_type = conf_fanpage.type
                self.routing_media_code = conf_fanpage.media_code
                self.routing_code = conf_fanpage.code
                self.type = "fanpage"
                return {"status": True}

        # id cant found
        return {"status": None}


    def send(self):
        # return lead_id
        if self.routing_type == "recruit":
            send = self.send_recruit()
            return send
        if self.routing_type == "franchise":
            send = self.send_franchise()
            return send
        if self.routing_type == "insurance":
            send = self.send_insurance()
            return send

    def send_recruit(self):
        response = requests.post(
            os.environ['ENV_SYSTEM_RECRUIT'],
            json=self.data_json,
        )
        json_response = response.json()
        if (json_response["success"]):
            json_response_arr = {"status": True, "message": json_response["data"]}
            return json_response_arr
        else:
            json_response_arr = {"status": None, "message": json_response}
            return json_response_arr

    def send_franchise(self):

        response = requests.post(
            os.environ['ENV_SYSTEM_ZATANNA'],
            json=self.data_json,
        )
        json_response = response.json()

        if (json_response["success"]):
            json_response_arr = {"status": True, "message": json_response["message"]}
            return json_response_arr
        else:
            json_response_arr = {"status": None, "message": json_response}
            return json_response_arr

    def send_insurance(self):

        response = requests.post(
            os.environ['ENV_SYSTEM_LMS'],
            json=self.data_json,
        )
        json_response = response.json()

        if (json_response["success"]):
            json_response_arr = {"status": True, "message": json_response["data"]}
            return json_response_arr
        else:
            json_response_arr = {"status": None, "message": json_response}
            return json_response_arr
