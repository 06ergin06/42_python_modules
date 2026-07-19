#!/usr/bin/env python3

import ex0
import typing


if __name__ == "__main__":
    flame_factory: ex0.FlameFactory = ex0.FlameFactory()
    aqua_factory: ex0.AquaFactory = ex0.AquaFactory()

    print("Testing factory")
    flame_base: typing.Any = flame_factory.create_base()
    print(flame_base.describe())
    print(flame_base.attack())

    flame_evolved: typing.Any = flame_factory.create_evolved()
    print(flame_evolved.describe())
    print(flame_evolved.attack())

    print()

    print("Testing factory")
    aqua_base: typing.Any = aqua_factory.create_base()
    print(aqua_base.describe())
    print(aqua_base.attack())

    aqua_evolved: typing.Any = aqua_factory.create_evolved()
    print(aqua_evolved.describe())
    print(aqua_evolved.attack())

    print()

    print("Testing battle")
    fighter1: typing.Any = flame_factory.create_base()
    fighter2: typing.Any = aqua_factory.create_base()

    print(fighter1.describe())
    print("vs.")
    print(fighter2.describe())
    print("fight!")
    print(fighter1.attack())
    print(fighter2.attack())
