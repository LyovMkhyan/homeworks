def missing_numbers(numbers: list) -> list:
    """
    :param numbers:
    :return list:
    """
    numbers = sorted(numbers)
    missing_nums = []
    for num in range(numbers[0], numbers[-1]):
        if not num in numbers:
            missing_nums.append(num)
    return missing_nums


numbers = [int(elem) for elem in input('Enter numbers: ').split()]

print(missing_numbers(numbers))

