# -*- coding: utf-8 -*-
from abc import ABC, abstractmethod
from chalicelib.domain.entities.conf_campaigns import ConfCampaignsGateway

class ConfCampaignsRepository(ABC):

    @abstractmethod
    def find_by_id(self, ad_id) -> ConfCampaignsGateway:
        raise NotImplementedError

