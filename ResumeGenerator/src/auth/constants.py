from fastapi.security import OAuth2PasswordBearer
from google.auth.transport import requests as google_requests

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")
firebase_request_adapter = google_requests.Request()
