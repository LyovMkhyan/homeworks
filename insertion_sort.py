def insertion_sort(numbers: list) -> list:
    """

    :param numbers:
    :return:
    """
    for index in range(len(numbers)):
        value_to_insert = numbers[index]
        previous_elem_index = index - 1
        while previous_elem_index >= 0 and numbers[previous_elem_index] > value_to_insert:
            numbers[previous_elem_index + 1], numbers[previous_elem_index] = numbers[previous_elem_index], numbers[previous_elem_index + 1]
            previous_elem_index = previous_elem_index - 1
    return numbers


numbers = [int(elem) for elem in input("Enter numbers: ").split()]
print(insertion_sort(numbers))