class LightBulb:
    def turn_on(self):
        print("LightBulb: turned on...")

    def turn_off(self):
        print("LightBulb: turned off...")


class ElectricPowerSwitch:
    def __init__(self, l: LightBulb) -> None:
        self.light_bulb = l
        self.on = False

    def press(self):
        if self.on:
            self.light_bulb.turn_off()
            self.on = False
        else:
            self.light_bulb.turn_on()
            self.on = True


if __name__ == "__main__":
    l = LightBulb()
    switch = ElectricPowerSwitch(l)
    switch.press()
    switch.press()
