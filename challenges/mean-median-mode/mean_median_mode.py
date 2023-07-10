"""Module to calculate the mean, median, and mode of a set of numbers."""


def calc_mean(numbers: list[int]) -> float:
    """
    Calculates the average of a list of numbers.

    Given a list of numbers, calculate the sum then divide them by the
    total amount of numbers and round it.

    Notes:
        Rounds to three decimal places.

    Args:
        numbers (List[int]): A list of integers.

    Returns:
        float: Float represented mean, rounded to three decimal places.

    Examples:
        >>> nums = [6, 9, 1, 2, 6, 3, 7]
        >>> mean = calc_mean(nums)
        >>> print(mean)
        4.857

    """

    mean = sum(numbers) / len(numbers)
    return round(mean, 3)


def calc_mean(numbers: list[int]) -> float:
    """Return the mean of a list of numbers."""

    mean = sum(numbers) / len(numbers)
    rounded_mean = round(mean, 3)

    return rounded_mean


def calc_median(numbers: list[int]) -> float:
    """Return the median in a list of numbers."""

    sorted_numbers = sorted(numbers)

    length = len(sorted_numbers)
    midpoint_index = length // 2

    if length % 2:
        # odd
        median = float(sorted_numbers[midpoint_index])
    else:
        # even
        upper_value = sorted_numbers[midpoint_index]
        lower_value = sorted_numbers[midpoint_index-1]
        median = (upper_value + lower_value) / 2

    rounded_median = round(median, 2)

    return rounded_median


def calc_mode(numbers: list[int]) -> list[int]:
    """Return the mode of a list of numbers."""

    frequency_dict = {}
    for unique_number in set(numbers):
        frequency = numbers.count(unique_number)
        frequency_dict[unique_number] = frequency

    highest = max(frequency_dict.values())

    modes = []
    for unique_number, frequency in frequency_dict.items():
        if frequency == highest:
            modes.append(unique_number)

    if len(modes) == len(frequency_dict.keys()):
        modes.clear()

    return modes


def solve_dataset(numbers: list[int]) -> tuple[float,
                                               float,
                                               list[int]]:
    """Return the mean, median, and mode of a data set."""

    mean = calc_mean(numbers)
    median = calc_median(numbers)
    mode = calc_mode(numbers)

    return mean, median, mode


def main() -> None:
    """Execute the main process."""

    data_set_one = [6, 9, 1, 2, 6, 3, 7]
    data_set_two = [6, 9, 1, 2, 6, 3, 7, 4]
    data_set_three = [6, 9, 1, 2, 6, 3, 7, 4, 1]
    data_set_four = [6, 9, 1, 2, 3, 7, 4, 8]

    data_sets = [data_set_one, data_set_two, data_set_three, data_set_four]

    for data_set in data_sets:
        mean, median, mode = solve_dataset(data_set)
        print(f"data_set={data_set}: "
              f"mean={mean}, median={median}, mode={mode}")


if __name__ == "__main__":
    main()
