def is_number_largest(number: int) -> bool:
    """
    :param number:
    :return:
    """
    # is_biggest = True
    while number > 10:
        digit = number % 10
        number //= 10
        if digit > number % 10:
            return False
    return True


print(is_number_largest(9414))

