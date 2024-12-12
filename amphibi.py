from animal import Animal

class Amphibi(Animal):
    def __init__(self, name, makanan, hidup, berkembang_biak, jenis_air, bernapas):
        super().__init__(name, makanan, hidup, berkembang_biak)
        self.jenis_air = jenis_air
        self.bernapas = bernapas

    def info_amphibi(self):
        super().info_animal(),
        print("jenis air \t\t\t :", self.jenis_air,
              "\nbernapas \t\t\t :", self.bernapas)
        


amphibi = Amphibi("Katak", "serangga", "dua alam", "bertelur", "air tawar","kulit dan paru2")
amphibi.info_amphibi()

print("================================")
amphibi = Amphibi("salamander", "serangga", "dua alam", "bertelur-beranak", "air tawar", "kulit, paru2, insang")
amphibi.info_amphibi()

print("================================")
amphibi = Amphibi("Axolotl", "serangga", "dua alam", "bertelur", "air tawar", "paru2 dan insang")
amphibi.info_amphibi()