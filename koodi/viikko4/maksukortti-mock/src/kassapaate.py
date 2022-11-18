HINTA = 5
from maksukortti import Maksukortti

class Kassapaate:
    def __init__(self):
        self.myytyja_lounaita = 0

    def lataa(self, kortti, summa):
        if summa > 0:
            kortti.lataa(summa)

    def osta_lounas(self, maksukortti):
        if maksukortti.saldo >= HINTA:
            maksukortti.osta(HINTA)
            self.myytyja_lounaita += 1
        else:
            pass
