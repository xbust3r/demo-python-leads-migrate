from sqlalchemy import MetaData, Table, Column, String, Integer, Text, SmallInteger, DateTime, sql, ForeignKey
from sqlalchemy.orm import mapper, clear_mappers, relationship
from chalicelib.domain.entities.facebook_leads import FacebookLeadsGateway

from chalicelib.domain.entities.facebook_ads import FacebookAdsGateway
from chalicelib.domain.entities.facebook_adsets import FacebookAdSetsGateway
from chalicelib.domain.entities.facebook_campaigns import FacebookCampaignsGateway
from chalicelib.domain.entities.facebook_brands import FacebookBrandsGateway

from chalicelib.domain.entities.conf_ads import ConfAdsGateway
from chalicelib.domain.entities.conf_adsets import ConfAdSetsGateway
from chalicelib.domain.entities.conf_campaigns import ConfCampaignsGateway
from chalicelib.domain.entities.conf_fanpages import ConfFanpagesGateway

metadata = MetaData()

facebook_leads = Table(
    'facebook_leads',
    metadata,
    Column('id', Integer, primary_key=True, nullable=False, key='id'),
    Column('leadgen_id', Integer, nullable=True),
    Column('ad_id', Integer, ForeignKey('facebook_ads.ad_id'), nullable=True),
    Column('first_name', String(120), nullable=True),
    Column('last_name', String(120), nullable=True),
    Column('zip_code', String(5), nullable=True),
    Column('phone_number', String(10), nullable=True),
    Column('email', String(120), nullable=True),
    # Column('user_name', String(30), nullable=True),
    # Column('api_key', String(30), nullable=True),
    Column('created_at', DateTime, nullable=True),
    Column('updated_at', DateTime, nullable=True),
)
facebook_ads = Table(
    'facebook_ads',
    metadata,
    Column('ad_id', Integer, primary_key=True, nullable=False, key='ad_id'),
    Column('ad_set_id', String(50), ForeignKey('facebook_ad_sets.ad_set_id'), nullable=True),
    Column('name', String(50), nullable=True),
    Column('created_at', DateTime, nullable=True),
    Column('updated_at', DateTime, nullable=True),
)
facebook_ad_sets = Table(
    'facebook_ad_sets',
    metadata,
    Column('ad_set_id', Integer, primary_key=True, nullable=False, key='ad_set_id'),
    Column('campaign_id', String(50), ForeignKey('facebook_campaigns.campaign_id'), nullable=True),
    Column('name', String(50), nullable=True),
    Column('created_at', DateTime, nullable=True),
    Column('updated_at', DateTime, nullable=True),
)
facebook_campaigns = Table(
    'facebook_campaigns',
    metadata,
    Column('campaign_id', Integer, primary_key=True, nullable=False, key='campaign_id'),
    Column('fanpage_id', String(50),ForeignKey('facebook_brands.fanpage_id'), nullable=True),
    Column('name', String(50), nullable=True),
    Column('created_at', DateTime, nullable=True),
    Column('updated_at', DateTime, nullable=True),
)
facebook_brands = Table(
    'facebook_brands',
    metadata,
    Column('fanpage_id', Integer, primary_key=True, nullable=False, key='fanpage_id'),
    Column('name', String(50), nullable=True),
    Column('created_at', DateTime, nullable=True),
    Column('updated_at', DateTime, nullable=True),
)


conf_ads = Table(
    'facebook_conf_ads',
    metadata,
    Column('id', Integer, primary_key=True, nullable=False, key='id'),
    Column('type', String(50), nullable=True),
    Column('media_code', String(50), nullable=True),
    Column('code', String(50), nullable=True),
    Column('created_at', DateTime, nullable=True),
    Column('updated_at', DateTime, nullable=True),
)
conf_adsets = Table(
    'facebook_conf_adsets',
    metadata,
    Column('id', Integer, primary_key=True, nullable=False, key='id'),
    Column('type', String(50), nullable=True),
    Column('media_code', String(50), nullable=True),
    Column('code', String(50), nullable=True),
    Column('created_at', DateTime, nullable=True),
    Column('updated_at', DateTime, nullable=True),
)
conf_campaigns = Table(
    'facebook_conf_campaigns',
    metadata,
    Column('id', Integer, primary_key=True, nullable=False, key='id'),
    Column('type', String(50), nullable=True),
    Column('media_code', String(50), nullable=True),
    Column('code', String(50), nullable=True),
    Column('created_at', DateTime, nullable=True),
    Column('updated_at', DateTime, nullable=True),
)
conf_fanpages = Table(
    'facebook_conf_pages',
    metadata,
    Column('id', Integer, primary_key=True, nullable=False, key='id'),
    Column('type', String(50), nullable=True),
    Column('media_code', String(50), nullable=True),
    Column('code', String(50), nullable=True),
    Column('created_at', DateTime, nullable=True),
    Column('updated_at', DateTime, nullable=True),
)


def load_mapper():
    clear_mappers()
    mapper(FacebookLeadsGateway,
           facebook_leads,
           properties={'ads': relationship(FacebookAdsGateway)}
           )
    mapper(FacebookAdsGateway,
           facebook_ads,
           properties={'adsets': relationship(FacebookAdSetsGateway)}
           )
    mapper(FacebookAdSetsGateway,
           facebook_ad_sets,
           properties={'campaigns': relationship(FacebookCampaignsGateway)}
           )
    mapper(FacebookCampaignsGateway,
           facebook_campaigns,
           properties={'brands': relationship(FacebookBrandsGateway)}
           )
    mapper(FacebookBrandsGateway,
           facebook_brands,
           #properties={'campaigns': relationship(FacebookBrandsGateway)}
           )

    mapper(ConfAdsGateway, conf_ads)
    mapper(ConfAdSetsGateway, conf_adsets)
    mapper(ConfCampaignsGateway, conf_campaigns)
    mapper(ConfFanpagesGateway, conf_fanpages)
