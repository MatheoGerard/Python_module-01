class Plant:
    def __init__(self, name: str, height: float, height_spd: float, age: int) -> None:
        if name:
            self.name = name
        else:
            self.name = "default"
        if height_spd >= 0:
            self.height_spd = height_spd
        else:
            self.height_spd = 0
        self.set_height(height, 1)
        self.set_age(age, 1)

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
        self._height += self.height_spd

    def add_age(self) -> None:
        self._age += 1

    def show(self) -> str:
        return (
            f"{self.name}: {round(self.get_height(), 1)}cm,"
            f"{self.get_age()} days old"
        )

    def current_state(self) -> None:
        print("Current state: " + self.show())


class Flower(Plant):
    def __init__(self, name: str, height: float, height_spd: float, age: int, color: str):
        super().__init__(name, height, height_spd, age)
        self.set_color(color)
        self._is_bloom: bool = False

    def set_color(self, color) -> None:
        if color:
            self._color = color
        else:
            self._color = "default"
            print("color is not define")

    def get_color(self) -> str:
        return self._color

    def bloom(self) -> None:
        if not self._is_bloom:
            self._is_bloom = True

    def get_bloom_state(self) -> bool:
        return _is_bloom

    def print_bloom_state(self) -> str:
        if self._is_bloom:
            return f"{self.name} is blooming NICE"
        else:
           return f"{self.name} has not bloomed yet"

    def show(self) -> str:
        parent_info: str = super().show()
        return f"{parent_info}\nColor: {self.get_color()}\n{self.print_bloom_state()}"



def main():
    flower = Flower("Rose", 8, 8, 30, "red")
    print(flower.show())
    flower.bloom()
    print(flower.show())

if __name__ == "__main__":
    print("=== Garden Plant Types ===")
    print("=== Flower ===")
    main()







