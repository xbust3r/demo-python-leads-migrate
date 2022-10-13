# -*- coding: utf-8 -*-

class FacebookLeadsGateway:
    def __init__(
            self,
            _id: int,
            leadgen_id: str = None,
            ad_id: str = None,
            media_code: str = None,
            first_name: str = None,
            last_name: str = None,
            zip_code: str = None,
            phone_number: str = None,
            email: str = None,
            created_at: str = None,
            updated_at: str = None,
    ):
        self.id = _id
        self.leadgen_id = leadgen_id
        self.ad_id = ad_id
        self.media_code = media_code
        self.first_name = first_name
        self.last_name = last_name
        self.zip_code = zip_code
        self.phone_number = phone_number
        self.email = email
        self.created_at = created_at
        self.updated_at = updated_at
