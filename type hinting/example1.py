from typing import Literal


# Literal - в точности такое значение
def get_gps_coordinates() \
        -> dict[Literal['latitude'] | Literal['longitude'], float]:
    """Returns current coordinates"""
    return {"latitude": 10.0, "longitude": 20.0}
