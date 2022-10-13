from chalicelib.domain.entities.facebook_ads import FacebookAdsGateway
from chalicelib.infraestructure.repository.facebook_ads import FacebookAdsRepository

class FacebookLeadsGatewaySqlAlchemyRepository(FacebookAdsRepository):
    def __init__(self, adapter):
        self.__adapter = adapter

    def find_by_id(self, id:int) -> FacebookAdsGateway:
        return self.__adapter.session.query(FacebookAdsGateway). \
            filter(FacebookAdsGateway.id == id). \
            first()

    def find_by_leadgen_id(self, leadgen_id:int) -> FacebookAdsGateway:
        return self.__adapter.session.query(FacebookAdsGateway). \
            filter(FacebookAdsGateway.leadgen_id == id). \
            first()

    def create(self, lead_gateway: FacebookAdsGateway):
        try:
            return self.__adapter.create(FacebookAdsGateway)
        except Exception as e:
            raise e

    def update(self, lead_gateway: FacebookAdsGateway):
        try:
            return self.__adapter.update(FacebookAdsGateway)
        except Exception as e:
            raise e