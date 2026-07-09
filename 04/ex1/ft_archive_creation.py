#!/usr/bin/env python3

import sys
import typing


def main() -> None:
    if len(sys.argv) != 2:
        print("Usage: ft_archive_creation.py <file>")
        return
    print("=== Cyber Archives Recovery & Preservation ===")
    file_name: str = sys.argv[1]
    print(f"Accessing file '{file_name}'")
    try:
        file: typing.IO[str] = open(file_name, "r")
        print("---")
        content: str = file.read()
        print(content, end="")
        print("---")
        file.close()
        print(f"File '{file_name}' closed.")

        print("Transform data:")
        print("---")
        content_arc: str = content.replace("\n", "#\n")
        print(content_arc, end="")
        print("---")

        new_file_name: str = input("Enter new file name (or empty): ")
        if new_file_name == "":
            print("Not saving data.")
        else:
            print(f"Saving data to '{new_file_name}'")
            output: typing.IO[str] = open(new_file_name, "w")
            output.write(content_arc)
            output.close()
            print(f"Data saved in file '{new_file_name}'.")

    except (FileNotFoundError, PermissionError) as e:
        print(f"Error opening file '{file_name}': {e}")


if __name__ == "__main__":
    main()
