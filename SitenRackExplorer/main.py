from netbox_client import NetBoxClient
from models.site import Site
from models.rack import Rack
from models.device import Device

def main():
    client = NetBoxClient()
    sites_data = client.get_sites()

    sites = []

    for site_data in sites_data:
        site = Site(id=site_data["id"], name=site_data["name"])
        racks_data = client.get_racks_by_site(site.id)

        for rack_data in racks_data:
            rack = Rack(id=rack_data["id"], name=rack_data["name"])
            devices_data = client.get_devices_by_rack(rack.id)

            for device_data in devices_data:
                device = Device(
                    id=device_data["id"],
                    name=device_data["name"],
                    device_type=device_data["device_type"]["model"],
                    status=device_data["status"]["label"]
                )
                rack.add_device(device)

            site.add_rack(rack)

        sites.append(site)

    # Display output
    for site in sites:
        print(f"📍 {site}")
        for rack in site.racks:
            print(f"  ├── {rack}")
            for device in rack.devices:
                print(f"  │     └── {device.name} ({device.device_type}) [{device.status}]")
        print()

if __name__ == "__main__":
    main()
