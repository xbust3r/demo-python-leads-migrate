from chalicelib.infraestructure.repository.sqlalchemy.conf_ads import ConfAdsGatewaySqlAlchemyRepository
from chalicelib.infraestructure.repository.sqlalchemy.conf_adsets import ConfAdSetsGatewaySqlAlchemyRepository
from chalicelib.infraestructure.repository.sqlalchemy.conf_campaigns import ConfCampaignsGatewaySqlAlchemyRepository
from chalicelib.infraestructure.repository.sqlalchemy.conf_fanpages import ConfFanpagesGatewaySqlAlchemyRepository

from chalicelib.infraestructure.adapter.sql.sqlalchemy import SqlAlchemyAdapter


class configuration:
    sql_alchemy = None

    def __init__(self):
        self.sql_alchemy = SqlAlchemyAdapter()

    def find_ad(self, ad_id):
        obj_conf_ad = ConfAdsGatewaySqlAlchemyRepository(self.sql_alchemy).find_by_id(ad_id)
        if not obj_conf_ad:
            return None
        else:
            return obj_conf_ad

    def find_adset(self, adset_id):
        obj_conf_adset = ConfAdSetsGatewaySqlAlchemyRepository(self.sql_alchemy).find_by_id(adset_id)
        if not obj_conf_adset:
            return None
        else:
            return obj_conf_adset

    def find_campaign(self, campaign_id):
        obj_conf_campaign = ConfCampaignsGatewaySqlAlchemyRepository(self.sql_alchemy).find_by_id(campaign_id)
        if not obj_conf_campaign:
            return None
        else:
            return obj_conf_campaign

    def find_fanpage(self, fanpage_id):
        obj_conf_fanpage = ConfFanpagesGatewaySqlAlchemyRepository(self.sql_alchemy).find_by_id(fanpage_id)
        if not obj_conf_fanpage:
            return None
        else:
            return obj_conf_fanpage
