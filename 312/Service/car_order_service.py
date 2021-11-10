from typing import List

from Domain.car_order import CarOrder
from Repository.car_order_repository import CarOrderRepository
from Repository.car_repository import CarRepository
from Repository.location_repository import LocationRepository


class CarOrderService:
    def __init__(self,
                 car_order_repository: CarOrderRepository,
                 car_repository: CarRepository,
                 location_repository: LocationRepository):
        self.car_order_repository = car_order_repository
        self.car_repository = car_repository
        self.location_repository = location_repository

    def add_car_order(self,
                      id_car_order: str,
                      id_car: str,
                      id_location: str,
                      cost_per_km: float):
        """
        TODO
        """
        car_order = CarOrder(id_car_order, id_car, id_location, cost_per_km)

        # ar merge si intr-un validator
        if self.car_repository.read(id_car) is None:
            raise KeyError(f'Nu exista masina cu id-ul {id_car}')
        if self.location_repository.read(id_location) is None:
            raise KeyError(f'Nu exista locatie cu id-ul {id_location}')

        self.car_order_repository.create(car_order)

    def update_car_order(self,
                         id_car_order: str,
                         id_car: str,
                         id_location: str,
                         cost_per_km: float):
        """
        TODO
        """
        car_order = CarOrder(id_car_order, id_car, id_location, cost_per_km)

        # ar merge si intr-un validator
        if self.car_repository.read(id_car) is None:
            raise KeyError(f'Nu exista masina cu id-ul {id_car}')
        if self.location_repository.read(id_location) is None:
            raise KeyError(f'Nu exista locatie cu id-ul {id_location}')

        self.car_order_repository.update(car_order)

    def delete_car_order(self, id_car_order: str):
        self.car_order_repository.delete(id_car_order)

    def get_all(self) -> List[CarOrder]:
        return self.car_order_repository.read()
