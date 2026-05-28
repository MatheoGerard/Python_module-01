class Plant:
    def __init__(
        self, name: str, height: float, height_spd: float, age: int
    ) -> None:
        if name:
            self.name: str = name
        else:
            self.name = "default"
        if height_spd >= 0:
            self.height_spd: float = height_spd
        else:
            self.height_spd = 0
        self.set_height(height, 1)
        self.set_age(age, 1)

    def set_age(self, age: int, is_init=0) -> None:
        if age >= 0:
            self._age: int = age
            if is_init == 0:
                print(f"Age updated: {self._age} days")
        else:
            if is_init == 1:
                self._age = 0
            print(f"{self.name.capitalize()}: Error, age can't be negative")
            print("Age update rejected")

    def set_height(self, height: float, is_init=0) -> None:
        if height >= 0:
            self._height: float = height
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
            f"{self.name}: {round(self.get_height(), 1)}cm, "
            f"{self.get_age()} days old"
        )

    def current_state(self) -> None:
        print("Current state: " + self.show())


def ft_garden_security() -> None:
    created = Plant("Rose", 8, 8, 3)
    created.current_state()
    print()
    created.set_age(30)
    created.set_height(188)
    print()
    created.current_state()
    print()
    created.set_age(-30)
    created.set_height(-188)
    print()
    created.current_state()


if __name__ == "__main__":
    print("=== Garden Security System ===")
    ft_garden_security()
