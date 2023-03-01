def num_to_sorted_number(number: int) -> int:
    number = str(number)
    list_of_digits = [digit for digit in number]
    sorted_list_of_digits = list(map(int, list_of_digits))
    sorted_list_of_digits.sort(reverse=True)
    sorted_number = ''
    for digit in sorted_list_of_digits:
        sorted_number += str(digit)
    sorted_number = int(sorted_number)
    return sorted_number


def is_number_largest(number: int) -> bool:
    if num_to_sorted_number(number) == number:
        return True
    else:
        return False


print(is_number_largest(2))
print(is_number_largest(678))
print(is_number_largest(888888889))
print(is_number_largest(65656540000))
print(is_number_largest(9441))
