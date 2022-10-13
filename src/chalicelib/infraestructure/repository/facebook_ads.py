# -*- coding: utf-8 -*-
from abc import ABC, abstractmethod
from chalicelib.domain.entities.facebook_ads import FacebookAdsGateway


class FacebookAdsRepository(ABC):

    @abstractmethod
    def find_by_id(self, id) -> FacebookAdsGateway:
        raise NotImplementedError

    @abstractmethod
    def find_by_leadgen_id(self, leadgen_id) -> FacebookAdsGateway:
        raise NotImplementedError
