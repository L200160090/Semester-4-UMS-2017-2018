"""soal 6"""
def apakahPrima(n):
    a = 0
    for i in range(1, n+1):
        if (n % i == 0):
            a += i
    if a == n+1:
         print(n, "adalah bilangan prima")
    else:
         print(n, "bukan bilangan prima")
        
def menghitungPrima(x):
    for i in range(2,x+1):
        apakahPrima(i)

