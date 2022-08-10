import string
import random


class VehicleInfo:
    brand: str
    catalogue_price: int
    electronic: bool

    def __init__(self, brand: str, catalogue_price: int, electronic: bool) -> None:
        self.brand = brand
        self.catalogue_price = catalogue_price
        self.electronic = electronic

    def compute_tax(self):
        tax_percentage = 0.05
        if self.electronic:
            tax_percentage = 0.02
        return tax_percentage * self.catalogue_price

    def print(self):
        print(f"Brand: {self.brand}")
        print(f"Payable tax: {self.compute_tax()}")


class Vehicle:
    vehicle_id: str
    license_plate: str
    info: VehicleInfo

    def __init__(self, id: str, license_plate: str, info: VehicleInfo) -> None:
        self.id = id
        self.license_plate = license_plate
        self.info = info

    def print(self):
        print(f"Id: {self.id}")
        print(f"License plate: {self.license_plate}")
        self.info.print()


class VehicleRegistry:
    vehicle_info: dict[str, VehicleInfo] = {}

    def __init__(self):
        self._add_vehicle_info("Tesla Model 3", 60000, True)
        self._add_vehicle_info("Volkswagen ID3", 35000, True)
        self._add_vehicle_info("BMW5", 45000, False)
        self._add_vehicle_info("Tesla Model Y", 75000, True)

    def _add_vehicle_info(
        self, brand: str, catalogue_price: int, electronic: bool
    ) -> None:
        self.vehicle_info[brand] = VehicleInfo(brand, catalogue_price, electronic)

    def generate_vehicle_id(self, length):
        return "".join(random.choices(string.ascii_uppercase, k=length))

    def generate_vehicle_license(self, id):
        return "-".join(
            [
                f"{id[:2]}",
                f"{''.join(random.choices(string.digits, k=2))}",
                f"{''.join(random.choices(string.ascii_uppercase, k=2))}",
            ]
        )

    def generate_vehicle(self, brand: str) -> Vehicle:
        vehicle_id = self.generate_vehicle_id(12)
        license_plate = self.generate_vehicle_license(vehicle_id)
        return Vehicle(vehicle_id, license_plate, self.vehicle_info[brand])


class Application:
    def register_vehicle(self, brand: string) -> Vehicle:
        # create a registry instance
        registry = VehicleRegistry()

        return registry.generate_vehicle(brand)


if __name__ == "__main__":
    app = Application()
    vehicle = app.register_vehicle("Volkswagen ID3")
    vehicle.print()
