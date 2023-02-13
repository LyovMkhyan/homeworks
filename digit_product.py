num = int(input('Enter a number: '))
prod = 1
while num > 0:
    if num % 10 != 0:
        prod *= num % 10
        num //= 10
    else:
        num //= 10

print(prod)
