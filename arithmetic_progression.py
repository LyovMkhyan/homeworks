a1,a2,n = map(int,input("Enter 2 numbers of progression and n: ").split(','))
d = a2 - a1
an = a1 + (n-1) * d
print(an)
