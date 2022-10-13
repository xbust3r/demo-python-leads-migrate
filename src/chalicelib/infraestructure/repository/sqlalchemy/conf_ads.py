from chalicelib.domain.entities.conf_ads import ConfAdsGateway
from chalicelib.infraestructure.repository.conf_ads import ConfAdsRepository


class ConfAdsGatewaySqlAlchemyRepository(ConfAdsRepository):
    def __init__(self, adapter):
        self.__adapter = adapter

    def find_by_id(self, ad_id: int) -> ConfAdsGateway:
        return self.__adapter.session.query(ConfAdsGateway). \
            filter(ConfAdsGateway.id == ad_id). \
            first()

    def create(self, conf_ads_gateway: ConfAdsGateway):
        try:
            return self.__adapter.create(ConfAdsGateway)
        except Exception as e:
            raise e

    def update(self, conf_ads_gateway: ConfAdsGateway):
        try:
            return self.__adapter.update(ConfAdsGateway)
        except Exception as e:
            raise e
