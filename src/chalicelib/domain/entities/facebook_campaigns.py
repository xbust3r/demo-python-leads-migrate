# -*- coding: utf-8 -*-

class FacebookCampaignsGateway:
    def __init__(
            self,
            campaign_id: int,
            fanpage_id: str = None,
            name: str = None,
            created_at: str = None,
            updated_at: str = None,

    ):
        self.campaign_id = campaign_id
        self.fanpage_id = fanpage_id
        self.name = name
        self.created_at = created_at
        self.updated_at = updated_at
