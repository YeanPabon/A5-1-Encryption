#Importacion de libreria
import numpy as np
#Inicializacion de datos
x=[1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1]
y=[1,1,0,0,1,1,0,0,1,1,0,0,1,1,0,0,1,1,0,0,1,1]
z=[1,1,1,0,0,0,0,1,1,1,1,0,0,0,0,1,1,1,1,0,0,0,0]
def maj(X,Y,Z):
    if (X==0):
        if (Y==0 or Z==0):
            m=0
        else:
            m=1
    else:
        if (Y==1 or Z==1):
            m=1
        else:
            m=0
    return m
for i in range (33):
    m=maj(x[8],y[10],z[10])
    #para x
    if x[8]==m:
        t=x[13]^x[16]^x[17]^x[18]
        for j in range(len(x)-1,0):
            if j==0:
                x[j]=t
            else:
                x[j]=x[j-1]
    s=""
    for j in x:
        s+=str(j)
    print("X: "+s)
    #para y
    if y[10]==m:
        t=y[20]^y[21]
        for j in range(len(y)-1,0):
            if j==0:
                y[j]=t
            else:
                y[j]=y[j-1]
    s=""
    for j in y:
        s+=str(j)
    print("Y: "+s)
    #para z
    if z[10]==m:
        t=z[7]^z[20]^z[21]^z[22]
        for j in range(len(z)-1,0):
            if j==0:
                z[j]=t
            else:
                z[j]=z[j-1]
    s=""
    for j in y:
        s+=str(j)
    print("Y: "+s)
    if i<32:
        key=x[len(x)-1]^y[len(y)-1]^z[len(z)-1]
        print("Keystream bit "+str(i)+" = "+str(x[len(x)-1])+"^"+str(y[len(y)-1])+"^"+str(z[len(z)-1])+"="+str(key))

