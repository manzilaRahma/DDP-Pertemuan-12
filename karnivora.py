from animal import Animal

class karnivora(Animal):
    def __init__(self, name, makanan, hidup, berkembang_biak, jenis_gigi, jenis_kuku):
        super().__init__(name, makanan, hidup, berkembang_biak)
        self.jenis_gigi = jenis_gigi
        self.jenis_kuku = jenis_kuku

    def info_karnivora(self):
        super().info_animal(),
        print("jenis gigi \t\t\t :", self.jenis_gigi,
              "\njenis kuku \t\t\t :", self.jenis_kuku)
        
macan = karnivora("macan", "daging", "darat", "melahirkan", "tajam", "cakar")
macan.info_karnivora()
print("===================")
beruang = karnivora("beruang", "daging", "darat", "melahirkan", "tajam", "cakar")
beruang.info_karnivora()
print("===================")
cheetah = karnivora("cheetah", "daging", "darat", "melahirkan", "tajam", "cakar")
cheetah.info_karnivora()
        