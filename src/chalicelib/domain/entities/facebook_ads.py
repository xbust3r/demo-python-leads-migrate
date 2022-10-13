# -*- coding: utf-8 -*-

class FacebookAdsGateway:
    def __init__(
            self,
            ad_id: int,
            ad_set_id: str = None,
            name: str = None,
            status: str = None,
            created_at: str = None,
            updated_at: str = None,

    ):
        self.ad_id = ad_id
        self.ad_set_id = ad_set_id
        #self.ad_id = ad_id
        self.name = name
        self.created_at = created_at
        self.updated_at = updated_at
