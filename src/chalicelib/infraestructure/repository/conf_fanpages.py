# -*- coding: utf-8 -*-
from abc import ABC, abstractmethod
from chalicelib.domain.entities.conf_fanpages import ConfFanpagesGateway

class ConfFanpagesRepository(ABC):

    @abstractmethod
    def find_by_id(self, ad_id) -> ConfFanpagesGateway:
        raise NotImplementedError

