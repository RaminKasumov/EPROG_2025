x = 4

def alpha(p):
    print("alpha(): local x =", 6)
    x = 6
    y = 0 + p

    def beta(q):
        nonlocal y
        y += 1
        y = y + q + p
        p_local = 2
        z = 1

        def gamma():
            global x
            global z
            nonlocal y
            y += 1
            z = 2
            x += 3
            w = 5
            print("inside gamma: global x =", x, ", global z =", z, ", local w =", w)

        comp = [k * k for k in range(3)]
        print("list comprehension creates a local k (0,1,2) that disappears afterwards")
        gamma()

    for i in range(2):
        beta(2)

    for i in range(2):
        x_inc = i
        print("incrementing global x by", i)

alpha(10)
print("final global x =", x)