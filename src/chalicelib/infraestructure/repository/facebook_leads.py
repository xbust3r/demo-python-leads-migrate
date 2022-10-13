# -*- coding: utf-8 -*-
from abc import ABC, abstractmethod
from chalicelib.domain.entities.facebook_leads import FacebookLeadsGateway


class FacebookLeadsRepository(ABC):

    @abstractmethod
    def find_by_id(self, id) -> FacebookLeadsGateway:
        raise NotImplementedError

    @abstractmethod
    def find_by_leadgen_id(self, leadgen_id) -> FacebookLeadsGateway:
        raise NotImplementedError
