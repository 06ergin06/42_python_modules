import elements
from . import elements as alch_elements


def healing_potion() -> str:
    earth: str = alch_elements.create_earth()
    air: str = alch_elements.create_air()
    return f"Healing potion brewed with '{earth}' and '{air}'"


def strength_potion() -> str:
    fire: str = elements.create_fire()
    water: str = elements.create_water()
    return f"Strength potion brewed with '{fire}' and '{water}'"
