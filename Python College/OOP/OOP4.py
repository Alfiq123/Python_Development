from OOP3 import Titik

tA = Titik('A', 10, 5)
tB = Titik('B', 16, 5)
tC = Titik('C', 10, 13)

tA.info()
tB.info()
tC.info()

jarakAB = tA.getJarak (tB)
jarakAC = tA.getJarak (tC)
jarakBC = tB.getJarak (tC)

print('Jarak A dan B =', jarakAB) 
print('Jarak A dan C =', jarakAC) 
print('Jarak B dan C =', jarakBC)
