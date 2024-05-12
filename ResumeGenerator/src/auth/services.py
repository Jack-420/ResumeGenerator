import json

import requests

from .models import VerifyPasswordResponse
from .utils import raise_detailed_error


def sign_in_with_email_and_password(email: str, password: str):
    # TODO remove the api key and place in env
    request_ref = "https://www.googleapis.com/identitytoolkit/v3/relyingparty/verifyPassword?key={0}".format(
        "AIzaSyB_CVh-sMWdcsdKdotLIED1DkimwBEfT2A"
    )
    headers = {"content-type": "application/json; charset=UTF-8"}
    data = json.dumps({"email": email, "password": password, "returnSecureToken": True})
    request_object = requests.post(request_ref, headers=headers, data=data, timeout=10)
    raise_detailed_error(request_object)
    return VerifyPasswordResponse(**request_object.json())
