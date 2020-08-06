#HEADPHONES _ PYTHON 3.8.3
###pruebas
#4 10 : 3
#8 9 : 2
# 8 8 : 1
datos=input().split()
M=int(datos[0])
N=int(datos[1])

if M<=20 and M>=2 and N>=1 and N<=20:
    division=int(N/M)
    residuo=N%M
    if residuo !=0:
        division=int(division)+1
        print(division)
    elif residuo ==0:
        print(division)

