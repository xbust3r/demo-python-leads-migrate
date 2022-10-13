# -*- coding: utf-8 -*-

class ConfAdsGateway:
    def __init__(
            self,
            _id: int,
            type: str = None,
            media_code: str = None,
            code: str = None,
            created_at: str = None,
            updated_at: str = None,

    ):
        self.id = _id
        self.type = type
        self.media_code = media_code
        self.code = code
        self.created_at = created_at
        self.updated_at = updated_at
