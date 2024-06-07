from enum import Enum

from pydantic import BaseModel


class UserClass(str, Enum):
    admin = "admin"
    user = "user"


class User(BaseModel):
    #     custom_claims = None
    # disabled = False
    # display_name = tester admin
    # email = test@gmail.com
    # email_verified = False
    # phone_number = None
    # photo_url = None
    # provider_data = [<firebase_admin._user_mgt.ProviderUserInfo object at 0x7f8d67fb47d0>]
    # provider_id = firebase
    # tenant_id = None
    # tokens_valid_after_timestamp = 1714555532000
    # uid = PvIyoDK04DVmnZcevPNG3YGVhp22
    # user_metadata = <firebase_admin._user_mgt.UserMetadata object at 0x7f8d65ebe950>
    uid: str
    email: str
    display_name: str
    email_verified: bool
    disabled: bool
    custom_claims: dict
    user_metadata: dict
    tokens_valid_after_timestamp: int
    phone_number: str
    photo_url: str
    provider_data: list
    provider_id: str
    tenant_id: str

    class Config:
        orm_mode = True
