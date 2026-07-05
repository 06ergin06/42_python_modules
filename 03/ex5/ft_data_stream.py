#!/usr/bin/env python3

import random
from typing import Generator


def gen_event() -> Generator[tuple[str, str], None, None]:
    players: list[str] = [
        "alice",
        "bob",
        "charlie",
        "dylan"
    ]
    actions: list[str] = [
        "run",
        "eat",
        "sleep",
        "grab",
        "move",
        "climb",
        "swim",
        "use",
        "release",
    ]
    while True:
        name: str = random.choice(players)
        action: str = random.choice(actions)
        yield (name, action)


def consume_event(
    event_list: list[tuple[str, str]],
) -> Generator[tuple[str, str], None, None]:
    while len(event_list) > 0:
        random_index: int = random.randint(0, len(event_list) - 1)
        event: tuple[str, str] = event_list[random_index]
        del event_list[random_index]
        yield event


def main() -> None:
    print("=== Game Data Stream Processor ===")
    stream: Generator[tuple[str, str], None, None] = gen_event()
    for i in range(1000):
        event: tuple[str, str] = next(stream)
        print(f"Event {i}: Player {event[0]} did action {event[1]}")
    event_list: list[tuple[str, str]] = []
    for _ in range(10):
        event_list += [next(stream)]
    print(f"\nBuilt list of 10 events: {event_list}")
    for event in consume_event(event_list):
        print(f"Got event from list: {event}")
        print(f"Remains in list: {event_list}")


if __name__ == "__main__":
    main()
