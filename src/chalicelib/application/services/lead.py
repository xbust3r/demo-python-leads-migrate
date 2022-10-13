import logging

from chalicelib.infraestructure.repository.sqlalchemy.facebook_leads import FacebookLeadsGatewaySqlAlchemyRepository
from chalicelib.infraestructure.adapter.sql.sqlalchemy import SqlAlchemyAdapter


class lead:
    id_lead = None
    sql_alchemy = None

    def __init__(self):

        self.sql_alchemy = SqlAlchemyAdapter()


    def get_lead(self, id_lead):

        obj_data = FacebookLeadsGatewaySqlAlchemyRepository(self.sql_alchemy).find_by_id(id_lead)
        if not obj_data:
            return None
        else:
            self.id_lead = obj_data.id
            logging.info("ads")
            return obj_data
