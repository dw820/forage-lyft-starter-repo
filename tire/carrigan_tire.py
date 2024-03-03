from serviceable.serviceable import Serviceable


class CarriganTire(Serviceable):
    def __init__(self, sensors):
        self.sensors = sensors

    def needs_service(self):

        for sensor in self.sensors:
            if sensor >= 0.9:
                return True

        return False