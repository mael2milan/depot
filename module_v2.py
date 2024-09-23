#!/bin/env python3
import sys, re

"""

Ce module permet l acquisition  de 3 manières différentes d'une liste

"""

def test():
    if len(sys.argv) == 1:
        print(False)
        print(sys.argv)
    elif len(sys.argv) == 2:
        print(True)
        print(sys.argv)
    else:
        print(sys.argv)

test()

# def test1():
#     while True:
#         line = input("? ").rstrip("\n").strip()
#         if line=="":
#             break
#         lline = re.split(r' +',line.rstrip("\n"))
#         print(lline)



# def acquisition():
#     if len(sys.argv) == 0:
#         """ Mode d acquisition par ligne interactive """ 
#         while True:
#             line = input("? ").rstrip("\n").strip()
#             if line=="":
#                 break
#             lline = re.split(r' +',line.rstrip("\n"))
#             i = 0
#             l = mklist()                      # rÃ©cupÃ©ration de la liste
#             tri(l)
#             print(f"{l=}")
#     elif len(sys.argv) == 1:
#         """ Mode d acquisition par lecture du nom de fichier source """
#         f = open(sys.argv[1], "r")
#     else:
#         """ Mode d acquisition par entrée directe des arguments """
#         def _construire():
#             nonlocal i  
#             l = []          
#             while True:
#                 if sys.argv[i]=="[":   
#                     i+=1               
#                     if i!=2:                  # pour la premiÃ¨re liste, on ne fait rien
#                         l.append(_construire()) 
#                 elif sys.argv[i]=="]":        # c'est la fin de la liste,
#                     i+=1
#                     return l                  # on renvoie la liste constuite
#                 else:                         # c'est une liste d'entiers
#                     l.append(int(sys.argv[i]))   
#                     i+=1
#         i = 1                              # indice pour parcourir les arguments
#         return _construire()
