year = int(input('Enter a year: '))
if year > 1 and year < 2023:
    century = year // 100
    if year % 100 > 1:
        print(century+1)
    else:
        print(century)
else:
    print("input number between 1 and 2023")
        

        