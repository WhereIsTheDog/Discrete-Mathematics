# -*- coding: utf-8 -*-
#Discrete Mathematics Exercise 1.3 30
#author: Caspter_ren


import itertools
import numpy as np


list1 = [[36,5],[264,9],[188,6],[203,8],[104,8],[7,6],[92,2],[65,8],[25,3],[170,6],[80,7],[22,4]]

weight,rating = zip(*list1)

for i in range(len(list1)):
    for j in itertools.combinations(weight,i):
        if(np.sum(j) == 700):
            print(j)
            list2=[]
            for k in j: 
                list2.append(rating[weight.index(k)])
            print(list2)
            print(np.sum(list2))