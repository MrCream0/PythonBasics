"""Module containing conditionals and loops in Python."""


def display_score(grade: int) -> None:
    """Showcase how conditionals work in Python."""

    if grade >= 93:
        print("You got an A!")
    elif grade >= 84 and grade < 93:
        print("You got a B!")
    elif grade < 84 and grade > 70:
        print("You passed...")
    else:
        print("You failed!")


def get_squares(numbers: list[int]) -> list[int]:
    """Showcase how loops work in Python."""

    squares = []
    for number in numbers:
        square = number ** 2  # number * number

        # if square < 10:
        #     continue

        # if square > 10:
        #     break

        squares.append(square)

    return squares


def main():
    """Execute the main process."""

    numbers = [1, 2, 3, 4, 5]
    squares = get_squares(numbers)
    print(squares)

    display_score(85)
    display_score(95)
    display_score(50)
    display_score(75)


if __name__ == "__main__":
    main()
