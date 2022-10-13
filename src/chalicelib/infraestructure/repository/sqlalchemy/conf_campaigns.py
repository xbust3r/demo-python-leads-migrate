from chalicelib.domain.entities.conf_campaigns import ConfCampaignsGateway
from chalicelib.infraestructure.repository.conf_campaigns import ConfCampaignsRepository


class ConfCampaignsGatewaySqlAlchemyRepository(ConfCampaignsRepository):
    def __init__(self, adapter):
        self.__adapter = adapter

    def find_by_id(self, adset_id: int) -> ConfCampaignsGateway:
        return self.__adapter.session.query(ConfCampaignsGateway). \
            filter(ConfCampaignsGateway.id == adset_id). \
            first()

    def create(self, ConfAdSetsGateway: ConfCampaignsGateway):
        try:
            return self.__adapter.create(ConfCampaignsGateway)
        except Exception as e:
            raise e

    def update(self, conf_adsets_gateway: ConfCampaignsGateway):
        try:
            return self.__adapter.update(ConfCampaignsGateway)
        except Exception as e:
            raise e
