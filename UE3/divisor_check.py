def divisor_check():
    n1 = int(input("Enter a number: "))
    n2 = int(input("Enter another number: "))

    if n1 > n2:
        return n1 % n2 == 0
    else:
        return n2 % n1 == 0

print(divisor_check())