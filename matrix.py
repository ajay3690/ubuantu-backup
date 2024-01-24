import sys                                  
sys.path.insert(0, './CoordGeo')        
import numpy as np
import numpy.linalg as LA
import scipy.linalg as SA
import math as m
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import pandas as pd
#local imports
from line.funcs import *
from triangle.funcs import *
from conics.funcs import circ_gen
#if using termux
import subprocess
import shlex
#end if
#Input parameters from excel file
df= pd.read_excel('vertices.xlsx')
#print(df ,"\n")
#Triangle Vertices
G_v= df.to_numpy()[:,:]
print("G_v=",G_v,"\n")
v1 = G_v[:, 0]
v2 = G_v[:, 1]
v3 = G_v[:, 2]
vn1=LA.norm(v1)
print(vn1)
A=v1/vn1
B1= v2 - (v2.T @ A )* A
vn2=LA.norm(B1)
B= B1/vn2
C1=v3-(v3.T @ A)*A-(v3.T @ B)*B
vn3=LA.norm(C1)
C= C1/vn3
print('A=',A)
print('B=',B)
print('C=',C)
print("***************gram schmidt matrix****************")
x=np.array((A,B,C))
print(x,"\n")
print("*********matrix after qr decomposition************")
y=x.T @ x
print(y,"\n")
u1=round((LA.norm(y[:,0])))
u2=round((LA.norm(y[:,1])))
u3=round((LA.norm(y[:,2])))
#print(u1)
#print(u2)
#print(u3)
if(u1==u2==u3):
    D=A+B+C
    print(D)
    nor4=LA.norm(D)
    nor1=LA.norm(A)
    nor2=LA.norm(B)
    nor3=LA.norm(C)
    print("nor1",nor1)
    print("nor2",nor2)
    print("nor3",nor3)
    print("nor4",nor4)
    #sample =((A.T @ D)/(nor1*nor4))
    #theta_1=np.degrees(np.arccos(sample))
    theta_1=np.degrees(np.arccos((A.T @ D)/(nor1*nor4)))
    theta_2=np.degrees(np.arccos((B.T @ D)/(nor2*nor4)))
    theta_3=np.degrees(np.arccos((C.T @ D)/(nor3*nor4)))
    print(theta_1)
    print(theta_2)
    print(theta_3)
    print("A+B+C equally inclined to A,B,C")
else:
    print("not inclined equally")
