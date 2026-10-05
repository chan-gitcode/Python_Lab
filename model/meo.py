from model.dong_vat import DongVat

class Meo(DongVat):
    def __int__(self):
        super().__init__()

    def chay(self):
        super().chay()
        print(f"{self._so_chan}")

    