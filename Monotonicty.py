numbers = [int(elem) for elem in input("Enter Numbers: ").split()]
is_ascending = True
is_descending = True
for i in range(len(numbers)-1):
    if numbers[i] <= numbers[i+1]:
        is_descending = False
    if numbers[i] >= numbers[i+1]:
        is_ascending = False

if is_ascending:
    print("Ascending")
elif is_descending:
    print("Descending")
else:
    print("Neither")
