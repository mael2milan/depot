#!/bin/env python3
import module_v2


def tri(l):
    """
    Cette fonction rÃ©cursive tri la liste passÃ©e en argument.
    """
    if type(l[0])==int:
        l.sort()
    else:
        for i in l:
            tri(i)


if __name__=="__main__":
    l = module_v2.acquisition()                      
    tri(l)
    print(f"{l=}")