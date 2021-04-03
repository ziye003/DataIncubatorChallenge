#!/usr/bin/env python
# coding: utf-8

# In[65]:


import random
import numpy as np
from decimal import Decimal
#M=20
M=5000
ls=[]
lc=[]
la=[]
for i in range(10000000000):
        s=0
        counter=0
        a=[]
        while s<M:
            a=random.randint(1,6)
            s+=a
            counter+=1
            a=s/counter
            pass
        ls.append(s)
        lc.append(counter)
        la.append(a)
pass
npls=np.array(ls)
meanM=str((Decimal(np.mean(npls))))
stdM=str(Decimal(np.std(npls)))
nplc=np.array(lc)
MeanC=str(Decimal(np.mean(nplc)))
npla=np.array(la)
MeanA=str(Decimal(np.mean(npla)))
f = open("m5000e10.txt", "x")
f.write(meanM)
f.write(stdM)
f.write(MeanC)
f.write(MeanA)
f.close()

