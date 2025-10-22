import requests
import os
from dotenv import load_dotenv
from models.site import Site
from models.rack import Rack
from models.device import Device
import urllib3

load_dotenv()
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

class NetBoxClient:
    def __init__(self):
        self.base_url = os.getenv("NETBOX_SERVER_URL")
        self.token = os.getenv("NETBOX_API_TOKEN")
        self.headers = {
            "Authorization": f"Token {self.token}",
            "Content-Type": "application/json",
            "Accept": "application/json"
        }

    def get(self, endpoint, params=None):
        url = f"{self.base_url}{endpoint}"
        response = requests.get(url, headers=self.headers, params=params, verify=False)
        if response.status_code == 200:
            return response.json()["results"]
        else:
            raise Exception(f"GET {url} failed: {response.status_code} - {response.text}")

    def get_sites(self):
        return self.get("dcim/sites/")

    def get_racks_by_site(self, site_id):
        return self.get("dcim/racks/", params={"site_id": site_id})

    def get_devices_by_rack(self, rack_id):
        return self.get("dcim/devices/", params={"rack_id": rack_id})
