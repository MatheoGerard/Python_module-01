class Plant:
    def __init__(self, name: str, height: float, spd: float, age: int) -> None:
        if name:
            self.name = name
        else:
            self.name = "default"
        if spd >= 0:
            self.spd = spd
        else:
            self.spd = 0
        self.set_height(height, 1)
        self.set_age(age, 1)
        self._stats = self._Stats()

    def set_age(self, age, is_init=0) -> None:
        if age >= 0:
            self._age = age
            if is_init == 0:
                print(f"Age updated: {self._age} days")
        else:
            if is_init == 1:
                self._age = 0
            print(f"{self.name.capitalize()}: Error, age can't be negative")
            print("Age update rejected")

    def set_height(self, height, is_init=0) -> None:
        if height >= 0:
            self._height = height
            if is_init == 0:
                print(f"Height updated: {self._height}cm")
        else:
            if is_init == 1:
                self._height = 0
            print(f"{self.name.capitalize()}: Error, height can't be negative")
            print("Height update rejected")

    def get_height(self) -> float:
        return self._height

    def get_age(self) -> int:
        return self._age

    def grow(self) -> None:
        self._height += self.spd
        self._stats.call_grow()

    def add_age(self) -> None:
        self._age += 1
        self._stats.call_age()

    class _Stats:
        def __init__(self) -> None:
            self._grow_call: int = 0
            self._add_age_call: int = 0
            self._show_call: int = 0

        def call_grow(self) -> None:
            self._grow_call += 1

        def call_age(self) -> None:
            self._add_age_call += 1

        def call_show(self) -> None:
            self._show_call += 1

        def get_grow_calls(self) -> int:
            return self._grow_call

        def get_age_calls(self) -> int:
            return self._add_age_call

        def get_show_calls(self) -> int:
            return self._show_call

        def display_stats(self) -> None:
            print(
                f"Stats: {self.get_grow_calls()} grow, {self.get_age_calls()} age, {self.get_show_calls()} show."
            )

    def display_stats(self) -> None:
        self._stats.display_stats()

    def show(self) -> None:
        print(
            f"{self.name}: {round(self.get_height(), 1)}cm, {self.get_age()} days old"
        )
        self._stats.call_show()

    def current_state(self) -> None:
        print("Current state: ", end="")
        self.show()

    @staticmethod
    def check_year(age) -> None:
        if age > 365:
            print(f"Is {age} days more than a year? -> True")
        else:
            print(f"Is {age} days more than a year? -> False")

    @classmethod
    def undefined_creator(cls):
        return cls(name="Unknown plant", height=0, spd=0, age=0)


class Flower(Plant):
    def __init__(self, name: str, height: float, spd: float, age: int, color: str):
        super().__init__(name, height, spd, age)
        self.set_color(color)
        self._is_bloom: bool = False

    def set_color(self, color) -> None:
        if color:
            self._color = color
        else:
            self._color = "default"
            print("color is not defined")

    def get_color(self) -> str:
        return self._color

    def bloom(self) -> None:
        if not self.get_bloom_state():
            self._is_bloom = True

    def get_bloom_state(self) -> bool:
        return self._is_bloom

    def print_bloom_state(self) -> str:
        if self.get_bloom_state():
            return f"{self.name} is blooming beautifully!"
        else:
            return f"{self.name} has not bloomed yet"

    def show(self) -> None:
        super().show()
        print(f"Color: {self.get_color()}\n{self.print_bloom_state()}")


class Tree(Plant):
    def __init__(
        self, name: str, height: float, spd: float, age: int, trunk_diameter: float
    ) -> None:
        super().__init__(name, height, spd, age)
        self.set_trunk_dia(trunk_diameter)

    def set_trunk_dia(self, trunk_diameter) -> None:
        if trunk_diameter >= 0:
            self.trunk_diameter = trunk_diameter
        else:
            self.trunk_diameter = 0
            print("trunk_diameter is not defined")

    def get_trunk_dia(self) -> float:
        return self.trunk_diameter

    def produce_shade(self) -> None:
        print(
            f"Tree Oak now produces a shade of {self.get_height()}cm long and {self.get_trunk_dia()} cm wide."
        )

    def show(self) -> None:
        super().show()
        print(f"Trunk diameter: {self.get_trunk_dia()}cm")


class Vegetable(Plant):
    def __init__(
        self, name: str, height: float, spd: float, age: int, harvest_season: str
    ) -> None:
        super().__init__(name, height, spd, age)
        self.set_harvest_season(harvest_season)
        self.set_nutritional_value()

    def set_harvest_season(self, harvest_season: str) -> None:
        if harvest_season:
            self._harvest_season = harvest_season
        else:
            self._harvest_season = "default"
            print("harvest_season is not defined")

    def get_harvest_season(self) -> str:
        return self._harvest_season

    def set_nutritional_value(self) -> None:
        self._nutritional_value = 0.0

    def nutritional_value_increase(self) -> None:
        self._nutritional_value += 0.5

    def grow(self) -> None:
        super().grow()
        self.nutritional_value_increase()

    def add_age(self) -> None:
        super().add_age()
        self.nutritional_value_increase()

    def get_nutritional_value(self) -> float:
        return self._nutritional_value

    def show(self) -> None:
        super().show()
        print(
            f"Harvest season: {self.get_harvest_season()}\nNutritional value: {int(self.get_nutritional_value())}"
        )


def main_check_year() -> None:
    plant = Plant("undefined", 60, 5, 75)
    Plant.check_year(plant.get_age())
    plant2 = Plant("undefined", 60, 5, 6548)
    Plant.check_year(plant2.get_age())


def main_flower() -> None:
    flower = Flower("Rose", 22, 1, 34, "Red")
    flower.show()
    print("[statistics for Rose]")
    flower.display_stats()
    print("[asking the rose to grow and bloom]")


def Unknown_plant_main() -> None:
    unknown_plant = Plant.undefined_creator()
    unknown_plant.show()


if __name__ == "__main__":
    print("=== Garden statistics ===")
    print("=== Check year-old")
    main_check_year()
    print("=== Flower")
    main_flower()
    print()
    print("=== Unknown plant")
    Unknown_plant_main()
