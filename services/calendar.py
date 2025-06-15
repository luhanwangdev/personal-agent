import os
from functools import lru_cache
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build


SCOPES = ['https://www.googleapis.com/auth/calendar']
CREDENTIALS_PATH = 'adk-test/credentials.json'
TOKEN_PATH = 'adk-test/token.json'

class CalendarService:
    def __init__(self):
        self.service = self._authenticate()
    
    def _authenticate(self):
        creds = None
        
        if os.path.exists(TOKEN_PATH):
            creds = Credentials.from_authorized_user_file('token.json', SCOPES)
        
        if not creds or not creds.valid:
            if creds and creds.expired and creds.refresh_token:
                print('refresh creds')
                creds.refresh(Request())
            else:
                print('flow')
                # credentials_path = os.path.join(os.path.dirname(os.path.dirname(__file__)), "credentials.json")
                flow = InstalledAppFlow.from_client_secrets_file(
                    CREDENTIALS_PATH, SCOPES)
                creds = flow.run_local_server(port=8080)
            
            with open(TOKEN_PATH, 'w') as token:
                token.write(creds.to_json())
        
        return build('calendar', 'v3', credentials=creds)


calendar_service = CalendarService()