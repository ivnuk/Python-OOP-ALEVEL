class Element:
    def __init__(self, t_melt, t_boil):
        self.t_melt = t_melt
        self.t_boil = t_boil

    def agg_state(self, temp: int, scale: str):
        temp = self.temp_convert(temp, scale)
        if temp < self.t_melt:
            return "solid"
        elif temp > self.t_boil:
            return "gas"
        return "liquid"

    def temp_convert(self, temp: int, scale: str = 'C'):
        if scale == 'F':
            return (temp-32)*5/9
        if scale == 'K':
            return temp - 273
        return temp

    def __str__(self):
        return f"Element with t_melting as {self.t_melt}"

class SuperElement(Element):
    def __init__(self, t_melt, t_boil, t_plasm):
        super().__init__(t_melt, t_boil)
        self.t_plasm = t_plasm

    def agg_state(self, temp: int, scale: str):
        state = super().agg_state(temp, scale)
        if state == 'gas' and  temp > self.t_plasm:
            return "plasm"


print(__name__)


if __name__ == "__main__":
    iron = Element(1000, 2862)
    neiron = Element(15, 290)
    print(iron)
    print(neiron.agg_state(1800, "F"))
