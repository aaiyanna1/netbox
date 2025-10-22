# client.py

import requests
import os
from dotenv import load_dotenv

# Note we use python dotenv to store NETBOX env variables and make them avail here.
load_dotenv()

class NetBoxClient:
    def __init__(self):
        self.base_url = os.getenv("NETBOX_SERVER_URL")
        self.token = os.getenv("NETBOX_API_TOKEN")
        self.headers = {
            "Authorization": f"Token {self.token}",
            "Content-Type": "application/json",
            "Accept": "application/json"
        }

    def get_devices(self, site=None, status=None, tenant=None):
        url = f"{self.base_url}dcim/devices/"
        params = {}

        if site:
            params["site"] = site
        if status:
            params["status"] = status
        if tenant:
            params["tenant"] = tenant

        response = requests.get(url, headers=self.headers, params=params, verify=False)

        if response.status_code == 200:
            return response.json()["results"]
        else:
            raise Exception(f"Error: {response.status_code} - {response.text}")
        
    def get_tenants(self, tenent=None):
        url = f"{self.base_url}tenancy/tenants"
        params = {} 
        
        if tenent:
            params["tenent"] = tenent

        response = requests.get(url, headers=self.headers, params=params, verify=False)

        if response.status_code == 200:
            return response.json()["results"]
        else:
            raise Exception(f"Error: {response.status_code} - {response.text}")


