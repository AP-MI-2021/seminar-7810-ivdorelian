from dataclasses import dataclass


@dataclass
class Location:
    id_location: str
    street_name: str
    street_number: int
