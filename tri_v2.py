#!/bin/env python3
import module_v2 as mod

l = mod.acquisition()

def tri(l):
    if type(l[0])==int:
        l.sort()
    else:
        for i in l:
            tri(i)

if __name__=="__main__":
    tri(l)
    print(f"{l=}")
