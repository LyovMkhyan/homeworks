number = int(input('Enter number between 1 and 10: '))
if number <= 10 and number >= 1:
    output_num = (10 ** number) - 1
    print(output_num)
else:
    print('Something went wrong pls try again! ')