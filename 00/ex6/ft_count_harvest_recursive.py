def ft_count_harvest_recursive() -> None:
    n = int(input("Days until harvest: "))

    def counter(day: int) -> None:
        if day > 0:
            counter(day - 1)
            print(f"Day {day}")
    counter(n)
    print("Harvest time!")
