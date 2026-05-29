import sys
import string


def parse_text(text: str) -> tuple:
    upper = 0
    lower = 0
    digit = 0
    space = 0
    punctuation = 0
    total = len(text)
    for char in text:
        if char.isupper():
            upper += 1
        elif char.islower():
            lower += 1
        elif char.isdigit():
            digit += 1
        elif char.isspace():
            space += 1
        elif char in string.punctuation:
            punctuation += 1
    return (total, upper, lower, punctuation, space, digit)


def build_result(counts: tuple) -> str:
    assert len(counts) == 6, "Invalid counts tuple"
    total, upper, lower, punctuation, space, digit = counts
    return (
        f"The text contains {total} characters:\n"
        f"{upper} upper letters\n"
        f"{lower} lower letters\n"
        f"{punctuation} punctuation marks\n"
        f"{space} spaces\n"
        f"{digit} digits"
    )


def main(argv: list) -> int:

    try:
        assert len(argv) <= 2, (
            "Too many arguments! Usage: python building.py"
        )

        if len(argv) == 1 or argv[1] is None:
            text = input("What is the text to count?\n")
            text += '\n'
        else:
            text = argv[1]

        counts = parse_text(text)
        print(build_result(counts))

    except AssertionError as e:
        print(f"AssertionError: {e}")
        sys.exit(1)
    except KeyboardInterrupt:
        print()
    except EOFError:
        pass
    except Exception as e:
        print(f"Error: {e}")
        sys.exit(1)
    return 0


if __name__ == "__main__":
    main(sys.argv)
