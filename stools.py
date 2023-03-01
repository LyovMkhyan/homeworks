def stools(numbers: str) -> int:
    numbers = numbers.split()
    maximum = int(numbers[0])
    sum_of_stools = 0
    for number in numbers:
        if maximum < int(number):
            maximum = int(number)
    for stool in numbers:
        sum_of_stools += maximum - int(stool)

    return sum_of_stools


print(stools("150 160 180 175"))
print(stools("150 150 150 150 150"))
print(stools("190 190 190 100 150 "))
print(stools("165"))
