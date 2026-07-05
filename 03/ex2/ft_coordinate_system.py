#!/usr/bin/env python3

import math


def main() -> None:
    print("=== Game Coordinate System ===\n")
    print("Get a first set of coordinates")
    t1: tuple[float, float, float] = get_player_pos()
    print(f"Got a first tuple: {t1}")
    x1, y1, z1 = t1
    print(f"It includes: X={x1}, Y={y1}, Z={z1}")
    distance1: float = round(math.sqrt(x1**2 + y1**2 + z1**2), 4)
    print(f"Distance to center: {distance1}\n")
    print("Get a second set of coordinates")
    t2: tuple[float, float, float] = get_player_pos()
    x2, y2, z2 = t2
    distance2: float = math.sqrt((x2 - x1)**2 + (y2 - y1)**2 + (z2 - z1)**2)
    print(f"Distance between the 2 sets of coordinates: {round(distance2, 4)}")


def get_player_pos() -> tuple[float, float, float]:
    while True:
        inp: str = input("Enter new coordinates as floats in format 'x,y,z': ")

        parts: list[str] = []
        temp: str = ""
        for char in inp:
            if char == ",":
                parts += [temp]
                temp = ""
            else:
                temp += char
        parts += [temp]

        length: int = 0
        for _ in parts:
            length += 1
        if length != 3:
            print("Invalid syntax")
            continue
        p: str = ""
        try:
            coords: list[float] = []
            for p in parts:
                coords += [float(p)]
            return (coords[0], coords[1], coords[2])
        except ValueError as e:
            print(f"Error on parameter '{p}': {e}")


if __name__ == "__main__":
    main()
