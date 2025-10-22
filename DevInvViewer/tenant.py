class Tenant:
    def __init__(self,id,name,slug,device_count) -> None:
        self.id = id
        self.name = name
        self.slug = slug
        self.device_count = device_count
        
    def display_tenants(self): 
        print(f"********** tenant_name = {self.name} **********")
        print(f"tenant_slug = {self.slug}")
        print(f"tenant_id = {self.id}")   
        print(f"device_count = {self.device_count}\n")