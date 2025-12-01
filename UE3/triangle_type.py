def triangle_type(a, b, c):
    sides = sorted([a, b, c])

    if sides[0] + sides[1] < sides[2]:
        return "impossible"
    elif sides[0] + sides[1] == sides[2]:
        return "degenerate"
    elif a == b == c:
        return "equilateral"
    elif a == b or b == c or a == c:
        return "isosceles"
    elif sides[0] ** 2 + sides[1] ** 2 == sides[2] ** 2:
        return "right-angled"
    else:
        return "scalene"

print(triangle_type(6, 3, 5))