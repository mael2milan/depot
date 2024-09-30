#!/bin/env python3
import module_v2

l = module_v2.acquisition()

def profondeur(l):
    def _profondeur(l,p):
        nonlocal prof
        for i in l:
            if type(i)==int:
                if p>prof:
                    prof = p
            else:
                _profondeur(i,p+1)
    prof=float("-inf")
    _profondeur(l,1)
    return(prof)
