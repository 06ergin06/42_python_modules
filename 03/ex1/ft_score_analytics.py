#!/usr/bin/env python3

import sys


def main() -> None:
    print("=== Player Score Analytics ===")
    scores: list[int] = []
    for arg in sys.argv[1:]:
        try:
            scores += [int(arg)]
        except ValueError:
            print(f"Invalid parameter: '{arg}'")
    if not scores:
        print(
            "No scores provided. Usage: "
            "python3 ft_score_analytics.py <score1> <score2> ..."
        )
        return
    max_scr: int = max(scores)
    min_scr: int = min(scores)
    sum_scr: int = sum(scores)
    len_scr: int = len(scores)
    print(f"Scores processed: {scores}")
    print(f"Total players: {len_scr}")
    print(f"Total score: {sum_scr}")
    print(f"Average score: {sum_scr / len_scr}")
    print(f"High score: {max_scr}")
    print(f"Low score: {min_scr}")
    print(f"Score range: {max_scr - min_scr}")


if __name__ == "__main__":
    main()
