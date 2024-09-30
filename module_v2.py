#!/bin/env python3
import sys, re

"""

Ce module permet l acquisition  de 3 manières différentes d'une liste

"""

def acquisition(): 
    if len(sys.argv) == 1:
        """ Acquisition interactive """
        def construire1():
            global i
            l = []          
            while True:
                if lline[i]=="[":   
                    i+=1                 
                    if i!=1:             
                        l.append(construire1())
                elif lline[i]=="]": 
                    i+=1
                    return l             
                else:
                    l.append(int(lline[i]))   
                    i+=1
        if __name__=="__main__":
            while True:
                line = input("? ").rstrip("\n").strip()
                if line=="":
                    break
                lline = re.split(r' +',line.rstrip("\n"))
                i = 0
                l = construire1()                      
                print(f"{l=}")
    elif len(sys.argv) == 2:
        """ Acquisition depuis un fichier source """
        def construire2(l0):
            def _construire2():
                nonlocal i
                l = []          # sous-liste courante
                while True:
                    if l0[i]=="[":   # c'est une sous-liste de listes
                        i+=1                 
                        if i!=1:             # pour la premiÃ¨re sous-liste, on ne fait rien
                            l.append(_construire2())    # sinon on construit cette sous-liste et on la met dans la sous-liste courante
                    elif l0[i]=="]": # c'est la fin de la sous-liste courante,
                        i+=1
                        return l             # on renvoie la sous-liste courante
                    else:                  # c'est une sous-liste d'entiers
                        l.append(int(l0[i]))   
                        i+=1
            i = 0
            return _construire2()
        listes_exploitables = []
        with open(sys.argv[1], "r") as f:
            for line in f:
                lline = re.split(r' +',line.strip())
                if lline:
                    liste = construire2(lline)
                    listes_exploitables.append(liste)
        return listes_exploitables
    else:
        """ Acquisition depuis la ligne de commande """
        def construire3():
                def _construire3():
                    nonlocal i  
                    l = []          
                    while True:
                        if sys.argv[i]=="[":   
                            i+=1               
                            if i!=2:                  
                                l.append(_construire3()) 
                        elif sys.argv[i]=="]":        
                            i+=1
                            return l                  
                        else:                         
                            l.append(int(sys.argv[i]))   
                            i+=1
                i = 1                              
                return _construire3()
        return construire3() #construit la liste de base

#print(acquisition())

def construire1():
    global i
    l = []          # liste courante
    while True:
        if lline[i]=="[":   # c'est une liste de listes
            i+=1                 # argument suivant
            if i!=1:             # pour la premiÃ¨re liste, on ne fait rien
                l.append(construire1())    # sinon on construit cette sous-liste et on la met dans la liste courante
        elif lline[i]=="]": # c'est la fin de la liste,
            i+=1
            return l             # on renvoie la liste courante
        else:                  # c'est une liste d'entiers
            l.append(int(lline[i]))   
            i+=1

if __name__=="__main__":
        # programme principal
    while True:
        line = input("? ").rstrip("\n").strip()
        if line=="":
            break
        lline = re.split(r' +',line.rstrip("\n"))
        i = 0
        l = construire1()                      # rÃ©cupÃ©ration de la liste
        return l

def construire2(l0):
    def _construire2():
        nonlocal i
        l = []          # sous-liste courante
        while True:
            if l0[i]=="[":   # c'est une sous-liste de listes
                i+=1                 
                if i!=1:             # pour la premiÃ¨re sous-liste, on ne fait rien
                    l.append(_construire2())    # sinon on construit cette sous-liste et on la met dans la sous-liste courante
            elif l0[i]=="]": # c'est la fin de la sous-liste courante,
                i+=1
                return l             # on renvoie la sous-liste courante
            else:                  # c'est une sous-liste d'entiers
                l.append(int(l0[i]))   
                i+=1
    i = 0
    return _construire2()


def construire3():
    def _construire3():
        nonlocal i  
        l = []          
        while True:
            if sys.argv[i]=="[":   
                i+=1               
                if i!=2:                  
                    l.append(_construire3()) 
                elif sys.argv[i]=="]":        
                    i+=1
                    return l                  
                else:                         
                    l.append(int(sys.argv[i]))   
                    i+=1
        i = 1                              
    return _construire3()













def acquisition_reel():
    if len(sys.argv) == 1:
        construire1()
    elif len(sys.argv) == 2:
        listes_exploitables = []
        with open(sys.argv[1], "r") as f:
            for line in f:
                lline = re.split(r' +',line.strip())
                if lline:
                    liste = construire2(lline)
                    listes_exploitables.append(liste)
        return listes_exploitables
    else:
        return construire3()

acquisition_reel