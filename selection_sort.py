def selection_sort(numbers: list) -> list:
    """

    :param numbers:
    :return:
    """
    for i in range(len(numbers) - 1):
        minimal_index = i
        for j in range(i+1, len(numbers)):
            if numbers[j] < numbers[minimal_index]:
                minimal_index = j
        numbers[i], numbers[minimal_index] = numbers[minimal_index], numbers[i]
    return numbers


numbers = [int(elem) for elem in input("Enter numbers:").split()]
print(selection_sort(numbers))
