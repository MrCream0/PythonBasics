"""Module containing logic for Python functions."""


def add_five(number: int) -> int:
    """Add five to a number provided as a parameter."""

    return number + 5


def main():
    """Execute the main process."""

    result = add_five(10)
    print(result)


if __name__ == "__main__":
    main()
