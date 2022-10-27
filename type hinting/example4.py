from typing import NamedTuple


class Coordinates(NamedTuple):
    latitude: float
    longitude: float


def get_gps_coordinates() \
        -> Coordinates:
    """Returns current coordinates"""
    return Coordinates(**{"latitude": 10.0, "longitude": 20.0})
