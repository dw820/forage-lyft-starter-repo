from serviceable.serviceable import Serviceable


class SpindlerBattery(Serviceable):
    def __init__(self, last_service_date, current_date) -> None:
        self.last_service_date = last_service_date
        self.current_date = current_date

    def needs_service(self) -> bool:
        service_threshold_date = self.last_service_date.replace(
            year=self.last_service_date.year + 2
        )
        if service_threshold_date < self.current_date:
            return True
        else:
            return False
