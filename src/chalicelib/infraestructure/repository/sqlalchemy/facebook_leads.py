from chalicelib.domain.entities.facebook_leads import FacebookLeadsGateway
from chalicelib.infraestructure.repository.facebook_leads import FacebookLeadsRepository

class FacebookLeadsGatewaySqlAlchemyRepository(FacebookLeadsRepository):
    def __init__(self, adapter):
        self.__adapter = adapter

    def find_by_id(self, id:int) -> FacebookLeadsGateway:
        return self.__adapter.session.query(FacebookLeadsGateway). \
            filter(FacebookLeadsGateway.id == id). \
            first()

    def find_by_leadgen_id(self, leadgen_id:int) -> FacebookLeadsGateway:
        return self.__adapter.session.query(FacebookLeadsGateway). \
            filter(FacebookLeadsGateway.leadgen_id == id). \
            first()

    def create(self, lead_gateway: FacebookLeadsGateway):
        try:
            return self.__adapter.create(FacebookLeadsGateway)
        except Exception as e:
            raise e

    def update(self, lead_gateway: FacebookLeadsGateway):
        try:
            return self.__adapter.update(FacebookLeadsGateway)
        except Exception as e:
            raise e