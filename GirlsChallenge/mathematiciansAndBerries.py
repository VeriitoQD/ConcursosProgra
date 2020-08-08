#prueba:
#1 2   #c1 c2
#2 1   #c1/ c2 
#0 3   #c1 c2/
#resultado 1 1
a=[]
b=[]
for i in range(3):
    lista=input().split()
    a.insert(i,lista[0])
    b.insert(i,lista[1])

c1=int(a[2])#peso de la canasta vacia 1
c2=int(b[1])#peso de la canasta vacia 2
c1b=int(a[0])-c1#peso de las bayas 1
c2b=int(b[0])-c2#peso de las bayas 2
print(str(c1b)+' '+str(c2b))