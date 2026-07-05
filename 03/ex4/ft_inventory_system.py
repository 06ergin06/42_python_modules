#!/usr/bin/env python3

import sys


def parser(arg: str) -> dict[str, int]:
    if ":" not in arg:
        print(f"Error - invalid parameter '{arg}'")
        return {}
    i: int = 0
    for i in range(len(arg)):
        if arg[i] == ":":
            break
    try:
        x: int = int(arg[i + 1:])
    except ValueError as e:
        print(f"Quantity error for '{arg[:i]}': {e}")
        return {}
    return {arg[:i]: x}


def main() -> None:
    print("=== Inventory System Analysis === ")
    inventory: dict[str, int] = dict()
    if len(sys.argv) > 1:
        for arg in sys.argv[1:]:
            item_dict: dict[str, int] = parser(arg)
            if not item_dict:
                continue
            key: str = list(item_dict.keys())[0]
            if key in inventory:
                print(f"Redundant item '{key}' - discarding ")
            else:
                inventory.update(item_dict)
    print(f"Got inventory: {inventory}")
    print(f"Item list: {list(inventory.keys())}")
    sum_inv: int = sum(inventory.values())
    print(f"Total quantity of the {len(inventory)} items: {sum_inv}")

    item_list: list[str] = list(inventory.keys())
    for key in item_list:
        percentage: float = round((inventory[key] / sum_inv) * 100, 1)
        print(f"Item {key} represents {percentage}%")

    if item_list:
        most: str = item_list[0]
        least: str = item_list[0]
        for key in item_list:
            if inventory[key] > inventory[most]:
                most = key
            if inventory[key] < inventory[least]:
                least = key
        print(f"Item most abundant: {most} with quantity {inventory[most]}")
        print(f"Item least abundant: {least} with quantity {inventory[least]}")
    inventory.update({"magic_item": 1})
    print(f"Updated inventory: {inventory}")


if __name__ == "__main__":
    main()
