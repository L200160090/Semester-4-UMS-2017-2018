from Soal2 import *

nama = raw_input("Masukkan nama Mahasiswa: ")
nim = raw_input("Masukkan nim Mahasiswa: ")
kota = raw_input("Masukkan kota tempat tinggal: ")
uang = int(raw_input("Masukkan jumlah uang saku per bulan: "))

soal3 = Mahasiswa(nama, nim, kota, uang)
print soal3
