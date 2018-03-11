class Pesan(object):
    """
	Sebuah class bernama Pesan.
	Untuk memahami konsep Class dan Object.
    """
    def __init__(self, sebuahString):
        self.teks = sebuahString
    def cetakIni(self):
	print self.teks
    def cetakPakaiHurufKapital(self):
	print str.upper(self.teks)
    def cetakPakaiHurufKecil(self):
	print str.lower(self.teks)
    def jumKar(self):
	return len(self.teks)
    def cetakJumlahKarakterku(self):
	print "Kalimatku mempunyai", len(self.teks), "karakter."
    def perbarui(self, stringBaru):
	self.teks = stringBaru

    #Metode untuk memeriksa suatu string terkandung di object Pesan itu.
    def apakahTerkandung(self, String2):
        self.teks2 = String2
        if self.teks2 in self.teks:
            print True
        else:
            print False

    #Metode untuk menghitung jumlah huruf konsonan
    def hitungKonsonan(self):
        a = ["q","w","r","t","y","p","s","d","f","g","h","j","k","l",
             "z","x","c","v","b","n","m"]
        b = 0
        for i in self.teks:
            if i.lower() in a:
                b += 1
        print b

    #Metode untuk menghitung jumlah huruf vokal
    def hitungVokal(self):
        a = ["a", "i", "u", "e", "o"]
        b = 0
        for i in self.teks:
            if i.lower() in a:
                b += 1
        print b
