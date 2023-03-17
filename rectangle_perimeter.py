def rectangle_perimeter(x1, x2, y1, y2, x3, y3, x4, y4) -> float:
    perimeter = (segment_length1(x1, x2, y1, y2) + segment_length2(x1, y1, x4, y4) + segment_length3(x2, y2, x3, y3) + segment_length4(x3, y3, x4, y4))
    return perimeter


def segment_length1(x1, x2, y1, y2):
    return (abs((x2 - x1)) * 2 + abs((y2 - y1)) * 2) ** 0.5


def segment_length2(x1, y1, x4, y4):
    return (abs((x1 - x4)) * 2 + abs((y1 - y4)) * 2) ** 0.5


def segment_length3(x2, y2, x3, y3):
    return (abs((x2 - x3)) * 2 + abs((y2 - y3)) * 2) ** 0.5


def segment_length4(x3, y3, x4, y4):
    return (abs((x3 - x4)) * 2 + abs((y3 - y4)) * 2) ** 0.5


print(rectangle_perimeter(0.5, 0.5, 0.5, 1.5, 1.5, 1.5, 1.5, 0.5))
