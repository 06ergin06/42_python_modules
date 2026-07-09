#!/usr/bin/env python3

import sys
import typing


def main() -> None:
    if len(sys.argv) != 2:
        print("Usage: ft_ancient_text.py <file>")
        return
    print("=== Cyber Archives Recovery ===")
    file_name: str = sys.argv[1]
    print(f"Accessing file '{file_name}'")
    try:
        file: typing.IO[str] = open(file_name, "r")
        print("---")
        print(file.read(), end="")
        print("---")
        file.close()
        print(f"File '{file_name}' closed.")
    except (FileNotFoundError, PermissionError) as e:
        print(f"Error opening file '{file_name}': {e}")


if __name__ == "__main__":
    main()
