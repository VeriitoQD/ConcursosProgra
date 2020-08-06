cadena=input()
tamanio=len(cadena)
if tamanio<1000:
    primer=cadena[0:1].capitalize()
    subcad=cadena[1:]
    print(primer+subcad)
else:
    exit