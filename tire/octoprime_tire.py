from serviceable.serviceable import Serviceable


class OctoprimeTire(Serviceable):
    def __init__(self, sensors):
        self.sensors = sensors

    def needs_service(self):
        return sum(self.sensors) >= 3
