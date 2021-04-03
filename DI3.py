#!/usr/bin/env python
# coding: utf-8

# In[65]:


import random
import numpy as np
from decimal import Decimal
ls=[]
lc=[]
la=[]
for i in range(10000000000):
        sum=0
        counter=0
        a=[]
        while sum<20:
            a=random.randint(1,6)
            sum+=a
            counter+=1
            a=sum/counter
            pass
        ls.append(sum)
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
f = open("m20e10.txt", "x")
f.write(meanM)
f.write(stdM)
f.write(MeanC)
f.write(MeanA)
f.close()

