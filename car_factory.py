from battery.nubbin_battery import NubbinBattery
from battery.spindler_battery import SpindlerBattery

from engine.capulet_engine import CapuletEngine
from engine.sternman_engine import SternmanEngine
from engine.willoughby_engine import WilloughbyEngine

from car import Car

"""
            Car	Engine	        Battery
Calliope	Capulet Engine	    Spindler Battery
Glissade	Willoughby Engine	Spindler Battery
Palindrome	Sternman Engine	    Spindler Battery
Rorschach	Willoughby Engine	Nubbin Batte
Thovex	    Capulet Engine	    Nubbin Battery

"""


class CarFactory:
    def create_calliope(
        current_date, last_service_date, current_mileage, last_service_mileage
    ) -> Car:
        engine = CapuletEngine(current_mileage, last_service_mileage)
        battery = SpindlerBattery(last_service_date, current_date)
        return Car(engine, battery)

    def create_glissade(
        current_date, last_service_date, current_mileage, last_service_mileage
    ) -> Car:
        engine = WilloughbyEngine(current_mileage, last_service_mileage)
        battery = SpindlerBattery(last_service_date, current_date)
        return Car(engine, battery)

    def create_palindrome(current_date, last_service_date, warning_light_on) -> Car:
        engine = SternmanEngine(warning_light_on)
        battery = SpindlerBattery(last_service_date, current_date)
        return Car(engine, battery)

    def create_rorschach(
        current_date, last_service_date, current_mileage, last_service_mileage
    ) -> Car:
        engine = WilloughbyEngine(current_mileage, last_service_mileage)
        battery = NubbinBattery(last_service_date, current_date)
        return Car(engine, battery)

    def create_thovex(
        current_date, last_service_date, current_mileage, last_service_mileage
    ) -> Car:
        engine = CapuletEngine(current_mileage, last_service_mileage)
        battery = NubbinBattery(last_service_date, current_date)
        return Car(engine, battery)
