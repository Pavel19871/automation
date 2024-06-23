
from address import address


class mailing:
    to_address = address
    from_address = address
    cost = "1500"
    track = "758"

    def __init__(self, to_address, from_address, cost, track):
        self.t = to_address
        self.f = from_address
        self.c = cost
        self.t = track

    def to_address(self):
        print(self.to_address)

    def from_address(self):
        print(self.from_address)
        
        