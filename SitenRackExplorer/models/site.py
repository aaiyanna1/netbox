class Site:
    def __init__(self, id, name):
        self.id = id
        self.name = name
        self.racks = []

    def add_rack(self, rack):
        self.racks.append(rack)

    def __str__(self):
        return f"Site: {self.name}"
