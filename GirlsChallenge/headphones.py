#prueba con M & N
#4 10 : 3
#8 9 : 2
#8 8 : 1
datos=input().split()
M=int(datos[0])
N=int(datos[1])
if M>=2 and M<=20 and N>=1 and N<=20:
    division=N/M
    residuo= N%M
    if residuo == 0:
        print(str(int(division)))
    elif residuo != 0:
        print(str(int(division)+1))
    else:
        exit

