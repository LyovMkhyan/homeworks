number = input('Enter a number: ')
half = len(number) // 2
sum1,sum2 = 0,0 
for index in range(len(number)):
    if index < half:
        sum1 += int(number[index])
    else:
        sum2 += int(number[index])

if sum1 == sum2 :
    print("Yes")
else:
    print("No")