# main.py

from client import NetBoxClient
from device import Device
from tenants import Tenants

def main():
    client = NetBoxClient()

    print("Fetching devices...")
    raw_devices = client.get_devices(tenant="data-core")

    devices = []
    for d in raw_devices:
        device = Device(
            id=d.get("id"),
            name=d.get("name"),
            device_type=d["device_type"]["model"],
            site=d["site"]["name"],
            status=d["status"]["label"],
            tenant =d["tenant"]["name"],
            tenant_id = d["tenant"]["id"]
        )
        devices.append(device)

    for device in devices:
        device.display()

if __name__ == "__main__":
    main()
