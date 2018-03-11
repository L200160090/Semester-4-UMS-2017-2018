"""soal 7"""
def faktorPrima(x):
    a = []
    b = 2
    while b <= x:
        if x % b == 0:
            a.append(b)
            x /= b
        else:
            b += 1
    print(a)

