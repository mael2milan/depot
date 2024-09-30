#!/bin/env python3
import module_v2 as mod 

l = mod.acquisition()  

def minmax(l):
    if type(l[0])==int:
        maxi.append(max(l))
    else:
        for i in l:
            minmax(i)

if __name__=="__main__":
    maxi = []
    minmax(l)
    print(min(maxi))