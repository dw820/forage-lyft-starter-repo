from serviceable.serviceable import Serviceable


class SternmanEngine(Serviceable):
    def __init__(self, warning_light_is_on):
        self.warning_light_is_on = warning_light_is_on

    def needs_service(self):
        if self.warning_light_is_on:
            return True
        else:
            return False
