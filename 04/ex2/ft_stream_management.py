#!/usr/bin/env python3

import sys
import typing


def main() -> None:
    if len(sys.argv) != 2:
        print("Usage: ft_stream_management.py <file>")
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
    except (FileNotFoundError, PermissionError) as e:
        print(
            f"[STDERR] Error opening file '{file_name}': {e}",
            file=sys.stderr
        )
        return

    print("Transform data:")
    print("---")
    content_arc: str = content.replace("\n", "#\n")
    if content and not content.endswith("\n"):
        content_arc += "#\n"
    print(content_arc, end="")
    print("---")

    print("Enter new file name (or empty): ", end="")
    sys.stdout.flush()
    n_file_name: str = sys.stdin.readline().strip('\n')
    if n_file_name == "":
        print("Not saving data.")
    else:
        print(f"Saving data to '{n_file_name}'")
        try:
            output: typing.IO[str] = open(n_file_name, "w")
            output.write(content_arc)
            output.close()
            print(f"Data saved in file '{n_file_name}'.")
        except (FileNotFoundError, PermissionError) as e:
            print(
                f"[STDERR] Error opening file '{n_file_name}': {e}",
                file=sys.stderr
            )
            print("Data not saved.")


if __name__ == "__main__":
    main()
