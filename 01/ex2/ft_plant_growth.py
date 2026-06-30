#!/usr/bin/env python3

class Plant:
    def __init__(self, name: str, height: float, age_days: int) -> None:
        self.name = name
        self.height = height
        self.age_days = age_days

    def grow(self, growth_rate: float = 0.8) -> None:
        self.height += growth_rate

    def age(self) -> None:
        self.age_days += 1

    def show(self) -> None:
        print(f"{self.name}: {self.height:.1f}cm, {self.age_days} days old")


def simulate_growth(plant: Plant, days: int) -> float:
    initial_height: float = plant.height

    for day in range(1, days + 1):
        print(f"=== Day {day} ===")
        plant.grow()
        plant.age()
        plant.show()

    final_height: float = plant.height
    total_growth: float = final_height - initial_height

    return round(total_growth, 1)


def main() -> None:
    rose: Plant = Plant("Rose", 25.0, 30)

    print("=== Garden Plant Growth ===")
    rose.show()

    total_weekly_growth: float = simulate_growth(rose, 7)
    print(f"Growth this week: {total_weekly_growth}cm")


if __name__ == "__main__":
    main()
