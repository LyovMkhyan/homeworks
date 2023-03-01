def is_number_largest(number: int) -> bool:
    is_biggest = True
    while number > 10:
        digit = number % 10
        number //= 10
        if digit > number % 10:
            is_biggest = False
            return is_biggest
        else:
            is_biggest = True
    return is_biggest


print(is_number_largest(9414))
