l1 = list(map(int,input('Enter nums with space: ').split(' ')))
prod = 1
for n in range(0,(len(l1)-1)):
    if n+1 > len(l1):
        prod = l1[n]
        break
    elif prod < l1[n] * l1[n+1]:
        prod = l1[n] * l1[n+1]
print(prod)
