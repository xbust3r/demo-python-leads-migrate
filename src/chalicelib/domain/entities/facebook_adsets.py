# -*- coding: utf-8 -*-

class FacebookAdSetsGateway:
    def __init__(
            self,
            ad_set_id: int,
            campaign_id: str = None,
            name: str = None,
            created_at: str = None,
            updated_at: str = None,

    ):
        self.ad_set_id = ad_set_id
        self.campaign_id = campaign_id
        self.name = name
        self.created_at = created_at
        self.updated_at = updated_at
