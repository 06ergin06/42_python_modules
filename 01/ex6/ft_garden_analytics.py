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

        self._grow_calls = 0
        self._age_calls = 0
        self._show_calls = 0

    @staticmethod
    def is_older_than_year(age_days: int) -> bool:
        return age_days > 365

    @classmethod
    def create_anonymous(cls) -> "Plant":
        return cls("Unknown plant", 0.0, 0)

    def get_height(self) -> float:
        return self._height

    def set_height(self, new_height: float) -> None:
        if new_height < 0:
            print(f"{self.name}: Error, height can't be negative")
        else:
            self._height = new_height

    def get_age(self) -> int:
        return self._age_days

    def set_age(self, new_age: int) -> None:
        if new_age < 0:
            print(f"{self.name}: Error, age can't be negative")
        else:
            self._age_days = new_age

    def grow(self, growth_rate: float = 0.8) -> None:
        self._grow_calls += 1
        self.set_height(self.get_height() + growth_rate)

    def age(self, days: int = 1) -> None:
        self._age_calls += 1
        self.set_age(self.get_age() + days)

    def show(self) -> None:
        self._show_calls += 1
        print(f"{self.name}: {self._height:.1f}cm, {self._age_days} days old")

    def display_statistics(self) -> None:
        print(
            f"Stats: {self._grow_calls} grow,"
            f"{self._age_calls} age, {self._show_calls} show"
        )


class Flower(Plant):
    def __init__(
        self, name: str, height: float, age_days: int, color: str
    ) -> None:
        super().__init__(name, height, age_days)
        self.color = color
        self.is_blooming = False

    def bloom(self) -> None:
        self.is_blooming = True

    def show(self) -> None:
        super().show()
        print(f"Color: {self.color}")
        if self.is_blooming:
            print(f"{self.name} is blooming beautifully!")
        else:
            print(f"{self.name} has not bloomed yet")


class Seed(Flower):
    def __init__(
        self, name: str, height: float, age_days: int, color: str
    ) -> None:
        super().__init__(name, height, age_days, color)
        self._seeds = 0

    def bloom(self, seeds: int = 0) -> None:
        super().bloom()
        self._seeds = seeds

    def show(self) -> None:
        super().show()
        print(f"Seeds: {self._seeds}")


class Tree(Plant):
    def __init__(
        self, name: str, height: float, age_days: int, trunk_diameter: float
    ) -> None:
        super().__init__(name, height, age_days)
        self.trunk_diameter = trunk_diameter
        self._shade_calls = 0

    def produce_shade(self) -> None:
        self._shade_calls += 1
        print(
            f"Tree {self.name} now produces a shade of "
            f"{self._height:.1f}cm long and {self.trunk_diameter:.1f}cm wide."
        )

    def show(self) -> None:
        super().show()
        print(f"Trunk diameter: {self.trunk_diameter:.1f}cm")

    def display_statistics(self) -> None:
        super().display_statistics()
        print(f"{self._shade_calls} shade")


def display_plant_statistics(plant: Plant) -> None:
    print(f"[statistics for {plant.name}]")
    plant.display_statistics()


def main() -> None:
    print("=== Garden statistics ===")

    print("=== Check year-old")
    print(f"Is 30 days more than a year? -> {Plant.is_older_than_year(30)}")
    print(f"Is 400 days more than a year? -> {Plant.is_older_than_year(400)}")

    print("=== Flower")
    rose = Flower("Rose", 15.0, 10, "red")
    rose.show()
    display_plant_statistics(rose)
    print("[asking the rose to grow and bloom]")
    rose.grow(8.0)
    rose.bloom()
    rose.show()
    display_plant_statistics(rose)

    print("\n=== Tree")
    oak = Tree("Oak", 200.0, 365, 5.0)
    oak.show()
    display_plant_statistics(oak)
    print("[asking the oak to produce shade]")
    oak.produce_shade()
    display_plant_statistics(oak)

    print("\n=== Seed")
    sunflower = Seed("Sunflower", 80.0, 45, "yellow")
    sunflower.show()
    print("[make sunflower grow, age and bloom]")
    sunflower.grow(30.0)
    sunflower.age(20)
    sunflower.bloom(42)
    sunflower.show()
    display_plant_statistics(sunflower)

    print("\n=== Anonymous")
    anonymous = Plant.create_anonymous()
    anonymous.show()
    display_plant_statistics(anonymous)


if __name__ == "__main__":
    main()
