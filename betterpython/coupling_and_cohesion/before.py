import string
import random


class VehicleRegistry:
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


class Application:
    def register_vehicle(self, brand: string):
        # create a registry instance
        registry = VehicleRegistry()

        # generate a vehicle id of length 12
        vehicle_id = registry.generate_vehicle_id(12)

        # now generate a license plate for the vehicle
        # using the first two charater of the vehicle id
        license_plate = registry.generate_vehicle_license(vehicle_id)

        # compute the catalogue price
        catalogue_price = 0
        if brand == "Tesla Model 3":
            catalogue_price = 60000
        elif brand == "Volkswagen ID3":
            catalogue_price = 35000
        elif brand == "BMW 5":
            catalogue_price = 45000

        # compute the tax percentage (default 5% of the catalogue price, except for electric car where it is 2%)
        tax_percentage = 0.05
        if brand in ["Tesla Model 3", "Volkswagen ID3"]:
            tax_percentage = 0.02

        # compute the payable tax
        payable_tax = tax_percentage * catalogue_price

        # print out the vehicle registration information
        print("Registration complete. Vehicle information:")
        print(f"Brand: {brand}")
        print(f"Id: {vehicle_id}")
        print(f"License plate: {license_plate}")
        print(f"Payable tax: {payable_tax}")


if __name__ == "__main__":
    app = Application()
    app.register_vehicle("Volkswagen ID3")
