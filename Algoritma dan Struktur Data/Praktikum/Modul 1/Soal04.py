"""Soal 4"""
def rerata(x):
    a = 0
    for i in range(len(x)):
       a += x[i]
    hasil = a / len(x)
    print(hasil)
