class Plant:
    def __init__(self, name: str, height: float, height_spd: float, age: int):
        if name:
            self.name = name
        else:
            self.name = "default"
        if height >= 0:
            self.set_height(height)
        else:
            self.set_height(0)
        if height_spd >= 0:
            self.height_spd = height_spd
        else:
            self.height_spd = .5
        if age >= 0:
            self.set_age(age)
        else:
            self.set_age(0)

    def set_age(self, age):
        if age >= 0:
            self._age = age
        else:
            print("invalid age")

    def get_age(self) -> int:
        return self._age

    def set_height(self, height):
        if height >= 0:
            self._height = height
        else:
            print("invalid height")

    def get_height(self) -> float:
        return self._height

    def grow(self):
        self._height += self.height_spd

    def add_age(self):
        self._age += 1

    def show(self) -> str:
        return f"{self.name}: {round(self._height, 1)}cm, {self._age} days old"


def ft_garden_security():
    rose = Plant("Rose", 8, 8, 3)
#    print(rose.show())
    print(f"ma plant a {rose.get_age()} jours, et fais {rose.get_height()} cm")
    rose.set_age(-30)
    rose.set_height(-18)
    print(f"ma plant a {rose.get_age()} jours, et fais {rose.get_height()} cm")
#    print(rose.show())


if __name__ == "__main__":
    ft_garden_security()
