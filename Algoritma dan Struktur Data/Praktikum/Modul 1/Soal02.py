"""Soal 2"""
def gambarlahPersegiEmpat(x,y):
     print("@" * y)
     for j in range(2,x):
         a = y - 2
         print("@" + (" " * a) + "@")
     print("@" * y)

