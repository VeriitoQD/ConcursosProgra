#pruebas
#1 3 4 : 4
#3 2 3 : 5

distancias=input().split()
d12=int(distancias[0])
d13=int(distancias[1])
d23=int(distancias[2])

suma_d1=d12+d13
suma_d2=d13+d23
suma_d3=d12+d23
if suma_d1<=suma_d2 and suma_d1<=suma_d3:
    print(suma_d1)
elif suma_d2<=suma_d1 and suma_d2<=suma_d3:
    print(suma_d2)
elif suma_d3<=suma_d1 and suma_d3<=suma_d2:
    print(suma_d3)
