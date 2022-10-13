# -*- coding: utf-8 -*-

class FacebookBrandsGateway:
    def __init__(
            self,
            fanpage_id: int,
            name: str = None,
            created_at: str = None,
            updated_at: str = None,

    ):
        self.fanpage_id = fanpage_id
        self.name = name
        self.created_at = created_at
        self.updated_at = updated_at
