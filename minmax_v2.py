#!/bin/env python3
import module_v2

l = module_v2.acquisition()  

def minmax(l):
    if type(l[0])==int:
        maxi.append(max(l))
    else:
        for i in l:
            minmax(i)

if __name__=="__main__":
    l = construire()
    maxi = []
    minmax(l)
    print(min(maxi))