import requests
from utils.config_reader import ConfigReader
class BaseApiClient:
    def __init__(self,base_url=None):
        self.base_url = base_url if base_url else ConfigReader.get_api_base_url()
        self.session = requests.Session() # Session keeps cookies/headers persistent across requests

    def get(self, endpoint, headers=None):
        """Send a GET request"""
        url = f"{self.base_url}/{endpoint}"
        response = self.session.get(url, headers=headers)
        return response

    def post(self, endpoint, payload=None, headers=None):
        """Send a POST request"""
        url = f"{self.base_url}/{endpoint}"
        response = self.session.post(url, json=payload, headers=headers)
        return response

    def put(self, endpoint, payload=None, headers=None):
        """Send a PUT request"""
        url = f"{self.base_url}/{endpoint}"
        response = self.session.put(url, json=payload, headers=headers)
        return response

    def delete(self, endpoint, headers=None):
        """Send a DELETE request"""
        url = f"{self.base_url}/{endpoint}"
        response = self.session.delete(url, headers=headers)
        return response