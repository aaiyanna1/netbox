#tenants.py

class Tenants:
    def __init__(self, id, name, display,slug):
        self.id = id
        self.name = name
        self.display = display
        self.slug = slug
    
    def displaytenants(self):
        print(f" Name: {self.name}")
        print(f" Id: {self.id}")
        print(f" Display: {self.display}")
        print(f" slug: {self.slug}")



    # "https://vm-vibnetbox.vib.local/api/tenancy/tenants/",