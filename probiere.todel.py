menge: dict = {}
for i, a in enumerate(range(1, 11), start=1):
    menge[i] = {
        a,
    }
    flag = True
    b = a
    k = 0
    while flag:
        k += 1
        b = 2 / b
        flag = k < 10
        menge[i] |= {b}
        if k >= 10:
            print("k")
    print(str(menge[i]))
