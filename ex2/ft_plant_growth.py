class Plant:
    def __init__(
        self, name: str, height: float, height_spd: float, age: int
    ) -> None:
        self.name: str = name
        self.height: float = height
        self.height_spd: float = height_spd
        self.age: int = age

    def grow(self) -> None:
        self.height += self.height_spd

    def add_age(self) -> None:
        self.age += 1

    def show(self) -> None:
        print(f"{self.name}: {round(self.height, 1)}cm, {self.age} days old")


def plant_evolution() -> None:
    rose = Plant("Rose", 25.0, 0.8, 30)
    print("=== Garden Plant Growth ===")
    rose.show()
    total_value: float = 0.0
    week = range(1, 8)
    for day in week:
        print(f"=== Day {day} ===")
        rose.grow()
        total_value += rose.height_spd
        rose.add_age()
        rose.show()
    print(f"Growth this week: {total_value}cm")


if __name__ == "__main__":
    plant_evolution()
