#!/usr/bin/env python3

def input_temperature(temp_str: str) -> int:
    temp_val: int = int(temp_str)
    if temp_val > 40:
        raise ValueError(f"{temp_val}°C is too hot for plants (max 40°C)")
    elif temp_val < 0:
        raise ValueError(f"{temp_val}°C is too cold for plants (min 0°C)")
    return temp_val


def test_temperature() -> None:
    print("=== Garden Temperature Checker ===")

    temp1: str = "25"
    print(f"Input data is '{temp1}'")
    try:
        temp_val1: int = input_temperature(temp1)
        print(f"Temperature is now {temp_val1}°C\n")
    except Exception as e:
        print(f"Caught input_temperature error: {e}\n")

    temp2: str = "abc"
    print(f"Input data is '{temp2}'")
    try:
        temp_val2: int = input_temperature(temp2)
        print(f"Temperature is now {temp_val2}°C\n")
    except Exception as e:
        print(f"Caught input_temperature error: {e}\n")

    temp3: str = "100"
    print(f"Input data is '{temp3}'")
    try:
        temp_val3: int = input_temperature(temp3)
        print(f"Temperature is now {temp_val3}°C\n")
    except Exception as e:
        print(f"Caught input_temperature error: {e}\n")

    temp4: str = "-50"
    print(f"Input data is '{temp4}'")
    try:
        temp_val4: int = input_temperature(temp4)
        print(f"Temperature is now {temp_val4}°C\n")
    except Exception as e:
        print(f"Caught input_temperature error: {e}\n")
    print("All tests completed program didn't crash!")


if __name__ == "__main__":
    test_temperature()
