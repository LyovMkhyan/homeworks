def binary_search(numbers: list, target: int, start: int, end: int) -> bool:
    '''
    :param numbers:
    :param target:
    :param start:
    :param end:
    :return:
    '''
    if start == end:
        return False
    mid = (start + end) // 2
    if target == numbers[mid]:
        return True
    if target < numbers[mid]:
        return binary_search(numbers, target, start, mid)
    return binary_search(numbers, target, mid+1, end)


nums = [1, 2, 3, 5, 23, 26, 41]
print(binary_search(nums, 1, 0, len(nums)))
