from array2D import slice_me

def test_exceptions():
    family = [[1.80, 78.4],
              [2.15, 102.7],
              [2.10, 98.5],
              [1.88, 75.2]]

    print("--- Test Normal ---")
    try:
        print(slice_me(family, 0, 2))
        print(slice_me(family, 1, -2))
    except Exception as e:
        print(f"Unexpected error: {e}")

    print("\n--- Test Exception: Not a list ---")
    try:
        print(slice_me("not a list", 0, 2))
    except ValueError as e:
        print(f"Caught expected error: {e}")

    print("\n--- Test Exception: Empty list ---")
    try:
        print(slice_me([], 0, 2))
    except ValueError as e:
        print(f"Caught expected error: {e}")

    print("\n--- Test Exception: Jagged list ---")
    jagged_family = [[1.80, 78.4], [2.15], [2.10, 98.5]]
    try:
        print(slice_me(jagged_family, 0, 2))
    except ValueError as e:
        print(f"Caught expected error: {e}")

if __name__ == "__main__":
    test_exceptions()
