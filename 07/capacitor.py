#!/usr/bin/env python3


import typing
import ex1


if __name__ == "__main__":
    print("Testing Creature with healing capability")
    healing_factory: ex1.HealingCreatureFactory = ex1.HealingCreatureFactory()

    print("base:")
    healing_base: typing.Any = healing_factory.create_base()
    print(healing_base.describe())
    print(healing_base.attack())
    print(healing_base.heal())

    print("evolved:")
    healing_evolved: typing.Any = healing_factory.create_evolved()
    print(healing_evolved.describe())
    print(healing_evolved.attack())
    print(healing_evolved.heal())

    print("\nTesting Creature with transform capability")
    trans_fact: ex1.TransformCreatureFactory = ex1.TransformCreatureFactory()

    print("base:")
    transform_base: typing.Any = trans_fact.create_base()
    print(transform_base.describe())
    print(transform_base.attack())
    print(transform_base.transform())
    print(transform_base.attack())
    print(transform_base.revert())

    print("evolved:")
    transform_evolved: typing.Any = trans_fact.create_evolved()
    print(transform_evolved.describe())
    print(transform_evolved.attack())
    print(transform_evolved.transform())
    print(transform_evolved.attack())
    print(transform_evolved.revert())
