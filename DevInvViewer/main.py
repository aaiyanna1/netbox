# main.py

from client import NetBoxClient
from device import Device
from tenant import Tenant

def main():
    client = NetBoxClient()

    print("Listing Tenants")
    netbox_tenants= client.get_tenants()

    tenants=[]
    for t in netbox_tenants:
        tenant = Tenant(
            name=t.get("name"),
            slug=t.get("slug"),
            id=t.get("id"),
            device_count=t.get("device_count") # maybe useful to get rack count.
        )
        tenants.append(tenant)
    
    for tenant in tenants:
        tenant.display_tenants()

    print("Choose a tenant from above list ^^  to Explore Devices \
        \n * Note *  Site and Status choices will be added later")
    user_input = input("Please enter tenant slug (def dunder-mifflin) : ") or "dunder-mifflin"

    print("Fetching devices...")
    raw_devices = client.get_devices(tenant=user_input) #Netbox operates with the slug concept.filter on slug NOT name

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
