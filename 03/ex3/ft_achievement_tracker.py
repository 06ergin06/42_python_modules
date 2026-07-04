#!/usr/bin/env python3

import random


def gen_player_achievements() -> set[str]:
    intra_achievements: set[str] = {
        "Bonus Hunter 1",
        "Bonus Hunter 2",
        "Code Explorer 1",
        "Code Explorer 2",
        "Happy 42nd Day!",
        "I don't know!",
        "I have no idea what I'm doing",
        "I'm reliable !",
        "It's a rich man's world 1",
        "Rigorous Basterd 1",
        "Welcome, Learner !",
        "Active Alumni",
        "Advanced Slayer 1",
        "All for One 1",
        "Ambassador",
    }
    achievements_len: int = random.randint(6, 9)
    return set(random.sample(list(intra_achievements), achievements_len))


def main() -> None:
    print("=== Achievement Tracker System ===\n")
    players: list[tuple[str, set[str]]] = [
            ("Alice", gen_player_achievements()),
            ("Bob", gen_player_achievements()),
            ("Charlie", gen_player_achievements()),
            ("Dylan", gen_player_achievements()),
    ]
    for name, achievements in players:
        print(f"Player {name}: {achievements}\n")
    print()

    all_ach: set[str] = set()
    for _, achievements in players:
        all_ach = set.union(all_ach, achievements)
    print(f"All distinct achievements: {all_ach}")
    print()

    common: set[str] = players[0][1]
    for _, achievements in players[1:]:
        common = set.intersection(common, achievements)
    print(f"Common achievements: {common}")
    print()

    for name, achievements in players:
        other_set: set[str] = set()
        for other_n, other_a in players:
            if name != other_n:
                other_set = set.union(other_set, other_a)
        exclusive: set[str] = set.difference(achievements, other_set)
        print(f"Only {name} has: {exclusive}")
    print()

    for name, achievements in players:
        print(f"{name} is missing: {set.difference(all_ach, achievements)}\n")


if __name__ == "__main__":
    main()
