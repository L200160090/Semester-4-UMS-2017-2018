"""Soal 9"""
def cetakAngka():
    a = "Python"
    b = "UMS"
    i = 1
    while i <= 100:
        if i % 3 == 0 and i % 5 == 0:
            print(a, b)
            i += 1
        elif i % 3 == 0:
            print(a)
            i += 1
        elif i % 5 == 0:
            print(b)
            i += 1
        else:
            print(i)
            i+= 1

