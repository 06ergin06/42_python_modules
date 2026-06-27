#!/usr/bin/env python3

def input_temperature(temp_str: str) -> int:
    return int(temp_str)


def test_temperature() -> None:
    print("=== Garden Temperature ===")

    temp1: str = "25"
    print(f"Input data is '{temp1}'")
    try:
        temp_val: int = input_temperature(temp1)
        print(f"Temperature is now {temp_val}°C\n")
    except Exception as e:
        print(f"Caught input_temperature error: {e}\n")

    temp2: str = "abc"
    print(f"Input data is '{temp2}'")
    try:
        input_temperature(temp2)
    except Exception as e:
        print(f"Caught input_temperature error: {e}\n")

    print("All tests completed program didn't crash!")


if __name__ == "__main__":
    test_temperature()
