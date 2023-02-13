date = int(input('Enter date: '))

if date % 4 != 0:
    print('No')
elif date % 100 != 0:
    print('Yes')
elif date % 400 == 0:
    print('Yes')
else:
    print('No')