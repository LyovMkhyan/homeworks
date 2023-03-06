def bubble_sort(numbers: list) -> list:
    is_swapped = True
    n = len(numbers)
    while is_swapped:
        is_swapped = False
        for i in range(n - 1):
            if numbers[i] > numbers[i + 1]:
                numbers[i], numbers[i + 1] = numbers[i + 1], numbers[i]
                is_swapped = True
    return numbers


numbers = [int(elem) for elem in input("enter nums:").split()]
print(bubble_sort(numbers))
