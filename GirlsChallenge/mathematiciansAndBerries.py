a=[]
b=[]
for i in range(0,3):
        comando=input().split()
        a.insert(i,int(comando[0]))
        b.insert(i,int(comando[1]))
c1=int(a[2])
c2=int(b[1])
pesoc1=int(a[0])-c1
pesoc2=int(b[0])-c2
print(str(pesoc1)+" "+ str(pesoc2))
