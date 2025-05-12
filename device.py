# device.py

class Device:
    def __init__(self, id, name, device_type, site, status, tenant, tenant_id):
        self.id = id
        self.name = name
        self.device_type = device_type
        self.site = site
        self.status = status
        self.tenant = tenant
        self.tenant_id = tenant_id

    def display(self):
        print(f"Device: {self.name}")
        print(f"  ID: {self.id}")
        print(f"  Type: {self.device_type}")
        print(f"  Site: {self.site}")
        print(f"  Status: {self.status}")
        print(f"  Tenant: {self.tenant}")
        print(f"  Tenant_Id: {self.tenant_id}")
        print("----")
