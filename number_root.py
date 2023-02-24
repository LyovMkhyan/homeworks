
def sum_of_digits(num: int) -> int:
    result = 0
    while num > 0:
        digit = num % 10
        num //= 10
        result += digit
    return result


def is_digit_tens(num: int) -> bool:
    if len(str(num)) > 1:
        return True


def number_root(number: int) -> int:
    while is_digit_tens(number):
        result = sum_of_digits(number)
        number = result
    return number


print(number_root(8))
print(number_root(78996))
print(number_root(10))
print(number_root(37100005))




# print(sum_of_digits(78996))