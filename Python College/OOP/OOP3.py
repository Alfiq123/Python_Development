
from math import sqrt
class Titik:
    _nama, _Xvalue, _Yvalue = "", 0, 0
    def __init__(self, nama, Xvalue, Yvalue): 
        self.setNama(nama)
        self.setposisiX(Xvalue)
        self.setposisiY(Yvalue)

    def setNama (self, nama):
        self.nama = nama

    def setposisiX(self, Xvalue):
        self.posisiX = Xvalue

    def setposisiY(self, Yvalue):
        self.posisiY = Yvalue

    def getNama(self): 
        return self.nama
    
    def getposisiX(self):
        return self.setposisiX
    
    def getposisiY(self):
        return self.setposisiY

    def info(self):
        print(self.nama, "(", self.posisiX, ",", self.posisiY, ")")

    def getJarak (pertama, kedua):
        deltaX = (pertama.posisiX - kedua.posisiX) ** 2
        deltaY = (pertama.posisiY - kedua.posisiY) ** 2
        jarak = sqrt(deltaX + deltaY)
        return jarak

