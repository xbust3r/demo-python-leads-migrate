from chalicelib.domain.entities.conf_fanpages import ConfFanpagesGateway
from chalicelib.infraestructure.repository.conf_fanpages import ConfFanpagesRepository


class ConfFanpagesGatewaySqlAlchemyRepository(ConfFanpagesRepository):
    def __init__(self, adapter):
        self.__adapter = adapter

    def find_by_id(self, campaign_id: int) -> ConfFanpagesGateway:
        return self.__adapter.session.query(ConfFanpagesGateway). \
            filter(ConfFanpagesGateway.id == campaign_id). \
            first()

    def create(self, ConfAdSetsGateway: ConfFanpagesGateway):
        try:
            return self.__adapter.create(ConfFanpagesGateway)
        except Exception as e:
            raise e

    def update(self, conf_adsets_gateway: ConfFanpagesGateway):
        try:
            return self.__adapter.update(ConfFanpagesGateway)
        except Exception as e:
            raise e
