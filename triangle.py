def triangle(a,b,c):
    max_side = max(a,b,c)
    min_side = min(a,b,c)
    other_side = ((a+b+c)-(max_side + min_side))
    if a + b > c and a + c > b and b + c > a:
        if max_side**2 ==  min_side**2 + other_side**2:
            print('Right triangle ')
        elif max_side**2 < other_side**2 +min_side**2:
            print('Acute triangle ')
        else:
            print('Obtuse  triangle ')
    else:
        print('Not a triangle  ')

triangle(4,5,3)
triangle(1,1,8)
triangle(6,5,4)
triangle(9,5,6)