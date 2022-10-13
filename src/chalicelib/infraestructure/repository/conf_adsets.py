# -*- coding: utf-8 -*-
from abc import ABC, abstractmethod
from chalicelib.domain.entities.conf_adsets import ConfAdSetsGateway


class ConfAdSetsRepository(ABC):

    @abstractmethod
    def find_by_id(self, ad_id) -> ConfAdSetsGateway:
        raise NotImplementedError

