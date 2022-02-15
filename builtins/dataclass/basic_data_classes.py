from dataclasses import dataclass, make_dataclass
from math import asin, cos, radians, sin, sqrt


@dataclass
class Position:
    name: str
    lon: float = 0.0
    lat: float = 0.0

    def distance_to(self, other: "Position"):
        r = 6371  # Earch radius in kilometers
        lam_1, lam_2 = radians(self.lon), radians(other.lon)
        phi_1, phi_2 = radians(self.lat), radians(other.lat)
        h = (
            sin((phi_2 - phi_1) / 2) ** 2
            + cos(phi_1) * cos(phi_2) * sin((lam_2 - lam_1) / 2) ** 2
        )
        return 2 * r * asin(sqrt(h))


Position2 = make_dataclass("Position", ["name", ("lat", float), ("lon", float, 0.0)])


if __name__ == "__main__":
    oslo = Position("Oslo", 10.8, 59.9)
    print(oslo)
    print(oslo.lat)
    print(f"{oslo.name} is at {oslo.lat}N, {oslo.lon}E")

    vancouver = Position("Vancouver", -123.1, 49.3)
    print(oslo.distance_to(vancouver))

    france = Position2("France", 2.2)
    print(france)
