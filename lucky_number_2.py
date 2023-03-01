def is_lucky(number: int) -> bool:
    number = str(number)
    sum_of_even_numbers = 0
    sum_of_odd_numbers = 0
    for i in range(len(number)):
        if i % 2 == 0:
            sum_of_even_numbers += int(number[i])
        else:
            sum_of_odd_numbers += int(number[i])
    if sum_of_odd_numbers == sum_of_even_numbers:
        return True
    else:
        return False



print(is_lucky(15224))
print(is_lucky(53143277))
print(is_lucky(121))
print(is_lucky(8))
print(is_lucky(10))