class Rack:
    def __init__(self, id, name):
        self.id = id
        self.name = name
        self.devices = []

    def add_device(self, device):
        self.devices.append(device)

    def __str__(self):
        return f"Rack: {self.name}"
