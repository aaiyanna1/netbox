class Device:
    def __init__(self, id, name, device_type, status):
        self.id = id
        self.name = name
        self.device_type = device_type
        self.status = status

    def __str__(self):
        return f"Device: {self.name} ({self.device_type}) - {self.status}"
