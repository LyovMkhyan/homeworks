date = int(input('Enter date: '))

if date % 4 == 0:
    if not date % 100 == 0:
        print('Yes')
    elif date % 100 == 0 and date % 400 == 0:
        print('Yes')
    else:
        print('No')
else:
    print('No')