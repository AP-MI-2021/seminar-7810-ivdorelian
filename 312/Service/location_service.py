from typing import List

from Domain.location import Location
from Repository.location_repository import LocationRepository


class LocationService:
    def __init__(self,
                 location_repository: LocationRepository):
        self.location_repository = location_repository

    def add_location(self,
                     id_location: str,
                     street_name: str,
                     street_number: int):
        """
        TODO
        """
        location = Location(id_location, street_name, street_number)
        self.location_repository.create(location)

    def update_location(self,
                        id_location: str,
                        street_name: str,
                        street_number: int):
        """
        TODO
        """
        location = Location(id_location, street_name, street_number)
        self.location_repository.update(location)

    def delete_location(self, id_location: str):
        self.location_repository.delete(id_location)

    def get_all(self) -> List[Location]:
        return self.location_repository.read()
