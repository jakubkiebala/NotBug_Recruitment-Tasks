numbers = [
    1, 5, 2, 3, 1, 4, 1, 23, 12, 2, 3, 1,
    2, 31, 23, 1, 2, 3, 1, 23, 1, 2, 3, 123
]


def list_with_first_ten_elements_sum(numbers_list):
    """
    Extracts a subset of 10 elements from the list, starting from the 5th element (index 4),
    and returns the subset.

    Args:
        numbers_list (list): The input list from which a subset will be extracted.

    Returns:
        list: A list containing 10 elements, starting from the 5th element of the input list.
    """
    subset = numbers_list[4:14]
    return subset


print(list_with_first_ten_elements_sum(numbers))
