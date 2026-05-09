class Plant:
    def __init__(self, name: str, height: float, height_spd: float, age: int):
        self.name = name
        self.height = height
        self.height_spd = height_spd
        self.age = age

    def grow(self):
        self.height += self.height_spd

    def add_age(self):
        self.age += 1

    def show(self):
        print(f"{self.name}: {round(self.height, 1)}cm, {self.age} days old")


def plant_factory():
    print("=== Plant Factory Output ===")

