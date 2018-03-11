"""Soal 3"""
def jumlahHurufVokal(x):
    vokal = ["a","i","u","e","o"]
    a = ""
    for i in x:
        if i in vokal:
           a += i
    listHasil = (len(x), len(a))
    print(listHasil)

 def jumlahHurufKonsonan(x):
     konsonan = ["q","w","r","t","y","p","s","d","f","g","h","j","k","l","z","x","c","v","b","n","m"]
     a = ""
     for i in x:
         if i in konsonan:
            a += i
     listHasil = (len(x), len(a))
     print(listHasil)


