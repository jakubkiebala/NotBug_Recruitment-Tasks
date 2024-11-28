def powers_of_2():
    """
    Generates a list of powers of 2 for n in the range [1..20].

    Returns:
        list: A list containing the powers of 2 from 2^1 to 2^20.
    """
    new_list = [2 ** n for n in range(1, 21)]
    return new_list


print(powers_of_2())
