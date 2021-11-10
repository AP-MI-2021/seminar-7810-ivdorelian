from Domain.car import Car
from Repository.car_repository import CarRepository
from utils import clear_file


def test_car_repository():
    filename = 'test_cars.json'
    clear_file(filename)
    car_repository = CarRepository(filename)
    added = Car('1', '32s', 'standard')
    car_repository.create(added)
    assert car_repository.read(added.id_car) == added
