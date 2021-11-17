from typing import List

from Domain.car import Car
from Domain.car_validator import CarValidator
from Repository.repository import Repository


class CarService:
    def __init__(self,
                 car_repository: Repository,
                 car_validator: CarValidator):
        self.car_repository = car_repository
        self.car_validator = car_validator

    def add_car(self,
                id_car: str,
                fleet_number: str,
                comfort_level: str,
                model: str):
        """
        TODO
        """
        car = Car(id_car, fleet_number, comfort_level, model)
        self.car_validator.validate(car)
        self.car_repository.create(car)

    def update_car(self,
                   id_car: str,
                   fleet_number: str,
                   comfort_level: str):
        """
        TODO
        """
        car = Car(id_car, fleet_number, comfort_level)
        self.car_validator.validate(car)
        self.car_repository.update(car)

    def delete_car(self, id_car: str):
        self.car_repository.delete(id_car)

    def get_all(self) -> List[Car]:
        return self.car_repository.read()
