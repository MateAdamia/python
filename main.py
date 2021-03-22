class book:
    def __init__(self,saxeli,avtori,gamoshveba,gverdebi):
        self._saxeli= saxeli
        self._avtori = avtori
        self._gamoshveba = gamoshveba
        self._gverdebi = gverdebi

    def get_saxeli(self):
        return self._saxeli
    def set_saxeli(self,saxeli):
         self._saxeli = saxeli

    def get_avtori(self):
        return self._avtori
    def set_avtori(self, avtori):
         self._avtori=avtori
    def get_gamoshveba(self):
        return self._gamoshveba
    def set_gamoshveba(self, gamoshveba):
        self._gamoshveba= gamoshveba
    def get_gverdebi(self):
        return self._gverdebi
    def set_gverdebi(self, gverdebi):
        self._gverdebi= gverdebi
    def info(self):
        print("saxeli:",self._saxeli,"avtori:",self._avtori,"gamoshvebis weli :",self._gamoshveba,"gverdebis raodenoba:",self._gverdebi)



wigni = book("tramalis mgeli","herman hese",1927,237)
print(wigni.info())
