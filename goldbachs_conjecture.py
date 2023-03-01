def is_prime(number):
    for num in range(2, int(number ** 0.5) + 1):
        if number % num == 0:
            return False
    return True


def is_number_goldbach(number: int) -> tuple[int, int]:
    if number > 2 and number % 2 == 0:
        for num in range(2,  (number // 2)+2):
            if is_prime(num) and is_prime(number-num):
                return num, number - num
    else:
        print("Input even number greater than 2")


print(is_number_goldbach(4))
print(is_number_goldbach(16))
print(is_number_goldbach(20))
print(is_number_goldbach(992))

