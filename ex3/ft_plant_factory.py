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

    def show(self) -> str:
        return f"{self.name}: {round(self.height, 1)}cm, {self.age} days old"


def plant_factory() -> None:
    plants = [
            Plant("Rose", 25.0, .8, 30),
            Plant("Oak", 200.0, .2, 365),
            Plant("Cactus", 5.0, .1, 90),
            Plant("Sunflower", 80.0, 1.2, 45),
            Plant("Fern", 15.0, .7, 120)
    ]
    for plant in plants:
        print("Created: " + plant.show())


if __name__ == "__main__":
    print("=== Plant Factory Output ===")
    plant_factory()
