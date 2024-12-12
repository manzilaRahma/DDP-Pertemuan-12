from animal import Animal

class mamalia(Animal):
    def __init__(self, name, makanan, hidup, berkembang_biak, jenis_kulit, ukuran_tubuh):
        super().__init__(name, makanan, hidup, berkembang_biak)
        self.jenis_kulit = jenis_kulit
        self.ukuran_tubuh = ukuran_tubuh

    def info_mamalia(self):
        super().info_animal(),
        print("jenis air \t\t\t :", self.jenis_kulit,
              "\nbernapas \t\t\t :", self.ukuran_tubuh)


kucing = mamalia("kucing", "ikan", "darat", "melahirkan", "berbulu", "kecil")
kucing.info_mamalia()
print("=============================")
gajah = mamalia("gajah", "tumbuhan", "darat", "melahirkan", "sedikit berbulu", "sangat besar")
gajah.info_mamalia()
print("=============================")
harimau = mamalia("harimau", "daging", "darat", "melahirkan", "berbulu", "besar")
harimau.info_mamalia()