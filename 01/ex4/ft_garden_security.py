#!/usr/bin/env python3

class Plant:
    def __init__(self, name: str, height: float, age_days: int) -> None:
        self.name = name
        if height < 0:
            print(f"{self.name}: Error, height can't be negative")
            self._height = 0.0
        else:
            self._height = height
        if age_days < 0:
            print(f"{self.name}: Error, age can't be negative")
            self._age_days = 0
        else:
            self._age_days = age_days

    def get_height(self) -> float:
        return self._height

    def set_height(self, new_height: float) -> None:
        if new_height < 0:
            print(f"{self.name}: Error, height can't be negative")
            print("Height update rejected")
        else:
            self._height = new_height
            print(f"Height updated: {new_height}cm")

    def get_age(self) -> int:
        return self._age_days

    def set_age(self, new_age: int) -> None:
        if new_age < 0:
            print(f"{self.name}: Error, age can't be negative")
            print("Age update rejected")
        else:
            self._age_days = new_age
            print(f"Age updated: {new_age} days")

    def show(self) -> None:
        print(f"{self.name}: {self._height:.1f}cm, {self._age_days} days old")


def main() -> None:
    print("=== Garden Security System ===")
    rose: Plant = Plant("Rose", 15.0, 10)
    print("Plant created: ", end="")
    rose.show()
    print()
    rose.set_height(25)
    rose.set_age(30)
    print()
    rose.set_height(-1)
    rose.set_age(-1)
    print()
    print("Current state: ", end="")
    rose.show()


if __name__ == "__main__":
    main()
