from chalicelib.domain.entities.conf_adsets import ConfAdSetsGateway
from chalicelib.infraestructure.repository.conf_adsets import ConfAdSetsRepository


class ConfAdSetsGatewaySqlAlchemyRepository(ConfAdSetsRepository):
    def __init__(self, adapter):
        self.__adapter = adapter

    def find_by_id(self, adset_id: int) -> ConfAdSetsGateway:
        return self.__adapter.session.query(ConfAdSetsGateway). \
            filter(ConfAdSetsGateway.id == adset_id). \
            first()

    def create(self, ConfAdSetsGateway: ConfAdSetsGateway):
        try:
            return self.__adapter.create(ConfAdSetsGateway)
        except Exception as e:
            raise e

    def update(self, conf_adsets_gateway: ConfAdSetsGateway):
        try:
            return self.__adapter.update(ConfAdSetsGateway)
        except Exception as e:
            raise e
