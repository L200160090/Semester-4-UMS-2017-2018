class Mahasiswa(object):
    def __init__(self, nama, NIM, kota, us):
        self.nama = nama
        self.NIM = NIM
        self.kotaTinggal = kota
        self.uangSaku = us
    def __str__(self):
        a = self.nama + "\nNIM : " + str(self.NIM) \
        + "\nTinggal di " + self.kotaTinggal \
        + "\nUang Saku Rp " + str(self.uangSaku) \
        + " tiap bulannya."
        return a
    def ambilNama(self):
        return self.nama
    def ambilNIM(self):
        return self.NIM
    def ambilUangSaku(self):
        return self.uangSaku

    #Metode untuk mengambil kota tinggal
    def ambilKotaTinggal(self):
        return self.kotaTinggal

    #Metode untuk memperbarui kota
    def perbaruiKotaTinggal(self, kotaBaru):
        self.kotaTinggal = kotaBaru

    #Metode untuk menambah uang saku
    def tambahUangSaku(self, uangBaru):
        self.uangSaku = self.uangSaku + uangBaru
