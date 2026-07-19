#!/usr/bin/env python3

import typing
import ex0
import ex1
import ex2


def battle(
    opponents: typing.List[typing.Tuple[
        ex0.CreatureFactory, ex2.BattleStrategy
    ]]
) -> None:
    print("*** Tournament ***")
    print(f"{len(opponents)} opponents involved")

    fighters: typing.List[typing.Tuple[typing.Any, ex2.BattleStrategy]] = []
    for factory, strategy in opponents:
        fighters.append((factory.create_base(), strategy))

    for i in range(len(fighters)):
        for j in range(i + 1, len(fighters)):
            creature1, strat1 = fighters[i]
            creature2, strat2 = fighters[j]

            print("* Battle *")
            print(creature1.describe())
            print("vs.")
            print(creature2.describe())
            print("now fight!")

            try:
                strat1.act(creature1)
                strat2.act(creature2)
            except ex2.StrategyError as e:
                print(f"Battle error, aborting tournament: {e}")
                return


if __name__ == "__main__":
    flame_factory = ex0.FlameFactory()
    aqua_factory = ex0.AquaFactory()
    healing_factory = ex1.HealingCreatureFactory()
    transform_factory = ex1.TransformCreatureFactory()

    # Stratejiler[cite: 1]
    normal_strat = ex2.NormalStrategy()
    aggressive_strat = ex2.AggressiveStrategy()
    defensive_strat = ex2.DefensiveStrategy()

    print("Tournament 0 (basic)")
    print("[(Flameling+Normal), (Healing+Defensive)]")
    battle([
        (flame_factory, normal_strat),
        (healing_factory, defensive_strat)
    ])
    print()

    print("Tournament 1 (error)")
    print("[(Flameling+Aggressive), (Healing+Defensive)]")
    battle([
        (flame_factory, aggressive_strat),
        (healing_factory, defensive_strat)
    ])
    print()

    print("Tournament 2 (multiple)")
    print("[(Aquabub+Normal), (Healing+Defensive), (Transform+Aggressive)]")
    battle([
        (aqua_factory, normal_strat),
        (healing_factory, defensive_strat),
        (transform_factory, aggressive_strat)
    ])
