#!/usr/bin/env python3


def secure_archive(
    file_name: str, action: str = "read", content: str = ""
) -> tuple[bool, str]:
    try:
        if action == "write":
            with open(file_name, "w") as file:
                file.write(content)
            return (True, "Content successfully written to file")
        else:
            with open(file_name, "r") as file:
                file_content: str = file.read()
            return (True, file_content)
    except (FileNotFoundError, PermissionError) as e:
        return (False, str(e))


def main() -> None:
    print("=== Cyber Archives Security ===")

    print("Using 'secure_archive' to read from a nonexistent file:")
    print(secure_archive("/not/existing/file", "read"))

    print("Using 'secure_archive' to read from an inaccessible file:")
    print(secure_archive("/etc/master.passwd", "read"))

    print("Using 'secure_archive' to read from a regular file:")
    result: tuple[bool, str] = secure_archive("ancient_fragment.txt", "read")
    print(result)

    print("Using 'secure_archive' to write previous content to a new file:")
    if result[0]:
        print(secure_archive("new_fragment.txt", "write", result[1]))
    else:
        print(secure_archive("new_fragment.txt", "write", "Fallback data"))


if __name__ == "__main__":
    main()
