#!/usr/bin/env python3

import random


def main() -> None:
    players: list[str] = [
        "Alice",
        "bob",
        "Charlie",
        "dylan",
        "Emma",
        "Gregory",
        "john ",
        "kevin",
        "Liam ",
    ]
    print(f"Initial list of players: {players}")
    cap_list: list[str] = [name.capitalize() for name in players]
    print(f"New list with all names capitalized: {cap_list}")
    only_cap: list[str] = [name for name in players if name[0].isupper()]
    print(f"New list of capitalized names only: {only_cap}")
    score_dict: dict[str, int] = {
        name: random.randint(50, 1000) for name in cap_list
    }
    print(f"Score dict: {score_dict}")
    avg_score: float = round(sum(score_dict.values()) / len(score_dict), 2)
    print(f"Score average is {avg_score}")
    high_scores: dict[str, int] = {
        name: score for name, score in score_dict.items() if score > avg_score
    }
    print(f"High scores: {high_scores}")


if __name__ == "__main__":
    main()
