class Animal:
    def __init__(self,saxeli,asaki):
        self._saxeli=saxeli
        self._asaki=asaki
    def info(self):
        print("saxeli:",self._saxeli,"","asaki:",self._asaki,"jishi:",self._jishi,"asaki:",self._asaki)
class Dog(Animal):
    def __init__(self,saxeli,asaki,jishi,feri):
        Animal.__init__(self,saxeli,asaki)
        self._jishi=jishi
        self._feri=feri

    def dog_info(self):
        print("jishi",self._jishi,"","feri:",self._feri)
cxoveli= Dog("chorna","4","pudedli","dasdw")
print(cxoveli.info())