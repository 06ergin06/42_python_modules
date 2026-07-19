import abc
import typing
from ex0.creatures import Creature
from ex1.capabilities import HealCapability, TransformCapability


class StrategyError(Exception):
    pass


class BattleStrategy(abc.ABC):
    @abc.abstractmethod
    def is_valid(self, creature: typing.Any) -> bool:
        pass

    @abc.abstractmethod
    def act(self, creature: typing.Any) -> None:
        pass


class NormalStrategy(BattleStrategy):
    def is_valid(self, creature: typing.Any) -> bool:
        return isinstance(creature, Creature)

    def act(self, creature: typing.Any) -> None:
        if not self.is_valid(creature):
            name: str = getattr(creature, "_name", "Unknown Creature")
            raise StrategyError(
                f"Invalid Creature '{name}' for this normal strategy"
            )

        print(creature.attack())


class AggressiveStrategy(BattleStrategy):
    def is_valid(self, creature: typing.Any) -> bool:
        return isinstance(creature, TransformCapability)

    def act(self, creature: typing.Any) -> None:
        if not self.is_valid(creature):
            name: str = getattr(creature, "_name", "Unknown Creature")
            raise StrategyError(
                f"Invalid Creature '{name}' for this aggressive strategy"
            )

        print(creature.transform())
        print(creature.attack())
        print(creature.revert())


class DefensiveStrategy(BattleStrategy):
    def is_valid(self, creature: typing.Any) -> bool:
        return isinstance(creature, HealCapability)

    def act(self, creature: typing.Any) -> None:
        if not self.is_valid(creature):
            name: str = getattr(creature, "_name", "Unknown Creature")
            raise StrategyError(
                f"Invalid Creature '{name}' for this defensive strategy"
            )

        print(creature.attack())
        print(creature.heal())
