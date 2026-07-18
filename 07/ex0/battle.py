#!/usr/bin/env python3
import ex0

if __name__ == "__main__":
    print("Testing factory ")
    flameling: ex0.FlameFactory = ex0.FlameFactory()
    print(f"{flameling.create_base()}")
    print(f"{flameling.create_evolved()}")
