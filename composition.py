class Laptop:
    def __init__(self, battery):
        self.battery = Battery(battery)


class Battery:
    def __init__(self, battery_type):
        self.battery_type = battery_type


laptop = Laptop()
