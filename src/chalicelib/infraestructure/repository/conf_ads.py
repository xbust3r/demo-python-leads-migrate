# -*- coding: utf-8 -*-
from abc import ABC, abstractmethod
from chalicelib.domain.entities.conf_ads import ConfAdsGateway


class ConfAdsRepository(ABC):

    @abstractmethod
    def find_by_id(self, adset_id) -> ConfAdsGateway:
        raise NotImplementedError

