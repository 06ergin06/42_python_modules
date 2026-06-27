#!/usr/bin/env python3


class Plant:
    class Statistics:
        def __init__(self) -> None:
            self.__grow_calls = 0
            self.__age_calls = 0
            self.__show_calls = 0

        def count_grow(self) -> None:
            self.__grow_calls += 1

        def count_age(self) -> None:
            self.__age_calls += 1

        def count_show(self) -> None:
            self.__show_calls += 1

        def display(self) -> None:
            print(
                f"Stats: {self.__grow_calls} grow, "
                f"{self.__age_calls} age, "
                f"{self.__show_calls} show"
            )

    def __init__(self, name: str, height: float, age_days: int) -> None:
        self.name = name
        self._height = height
        self._age_days = age_days
        self.__statistics = Plant.Statistics()

    @staticmethod
    def is_older_than_year(age_days: int) -> bool:
        return age_days > 365

    @classmethod
    def create_anonymous(cls) -> "Plant":
        return cls("Unknown plant", 0.0, 0)

    def _statistics(self) -> "Plant.Statistics":
        return self.__statistics

    def _set_statistics(self, statistics: "Plant.Statistics") -> None:
        self.__statistics = statistics

    def grow(self, growth_rate: float = 0.8) -> None:
        self._statistics().count_grow()
        self._height += growth_rate

    def age(self, days: int = 1) -> None:
        self._statistics().count_age()
        self._age_days += days

    def show(self) -> None:
        self._statistics().count_show()
        print(f"{self.name}: {self._height:.1f}cm, {self._age_days} days old")

    def display_statistics(self) -> None:
        self._statistics().display()


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
        self.__seeds = 0

    def bloom(self, seeds: int = 0) -> None:
        super().bloom()
        self.__seeds = seeds

    def show(self) -> None:
        super().show()
        print(f"Seeds: {self.__seeds}")


class Tree(Plant):
    class Statistics(Plant.Statistics):
        def __init__(self) -> None:
            super().__init__()
            self.__shade_calls = 0

        def count_shade(self) -> None:
            self.__shade_calls += 1

        def display(self) -> None:
            super().display()
            print(f"{self.__shade_calls} shade")

    def __init__(
        self, name: str, height: float, age_days: int, trunk_diameter: float
    ) -> None:
        super().__init__(name, height, age_days)
        self.__tree_statistics = Tree.Statistics()
        self._set_statistics(self.__tree_statistics)
        self.trunk_diameter = trunk_diameter

    def produce_shade(self) -> None:
        self.__tree_statistics.count_shade()
        print(
            f"Tree {self.name} now produces a shade of "
            f"{self._height:.1f}cm long and {self.trunk_diameter:.1f}cm wide."
        )

    def show(self) -> None:
        super().show()
        print(f"Trunk diameter: {self.trunk_diameter:.1f}cm")


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

    print("=== Tree")
    oak = Tree("Oak", 200.0, 365, 5.0)
    oak.show()
    display_plant_statistics(oak)
    print("[asking the oak to produce shade]")
    oak.produce_shade()
    display_plant_statistics(oak)

    print("=== Seed")
    sunflower = Seed("Sunflower", 80.0, 45, "yellow")
    sunflower.show()
    print("[make sunflower grow, age and bloom]")
    sunflower.grow(30.0)
    sunflower.age(20)
    sunflower.bloom(42)
    sunflower.show()
    display_plant_statistics(sunflower)

    print("=== Anonymous")
    anonymous = Plant.create_anonymous()
    anonymous.show()
    display_plant_statistics(anonymous)


if __name__ == "__main__":
    main()
