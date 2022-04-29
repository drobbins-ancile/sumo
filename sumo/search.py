import json
import requests
import datetime
from base64 import b64encode

deployment_endpoints = {
    "US1": "https://api.sumologic.com/api/v1/search/jobs"
}

class Search:
    
    def __init__(self, endpoint: str, query: dict, auth: dict):
        self.endpoint = endpoint
        self.query = query
        self.access_id = auth["access_id"]
        self.access_key = auth["access_key"]


    def build_session(self):

        session = requests.Session()

        creds = f"{self.access_id}:{self.access_key}"
        encodedBytes = b64encode(creds.encode("utf-8"))
        encodedStr = str(encodedBytes, "utf-8")
        headers = {
            "Authorization": "Basic %s" % encodedStr,
            "Content-Type": "application/json",
            "Accept": "application/json",
        }
        session.headers.update(headers)
        

    def get_job_id(self) -> str:

        r = self.session.post(self.endpoint, data=json.dumps(self.query))
        self.job_id = json.loads(r.text)["id"]