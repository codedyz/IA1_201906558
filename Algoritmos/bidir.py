import os
from successors import *

def bidir_analysis(ini, end, orden=True, dimen=True):
    front = [ini]
    back = [end]

    while front or back:
        nfront = front.pop(0)
        nback = back.pop(0)
        print(nfront)
        print(nback)
        if nfront in back and nback in front:
            if back.index(nfront) < front.index(nback):
                print(str(nfront)+" Front_comun")
                return
            else:
                print(str(nback)+" Back_comun")
                return
        elif nfront in back:
            print(str(nfront)+" Front_comun")
            return
        elif nback in front:
            print(str(nback)+" Back_comun")
            return
        

        if(dimen == False):
           front.extend(x4(nfront))
        else:
            front.extend(x3(nfront))

        print("front",front)
        

        if(dimen == False):
           back.extend(x4(nback))
        else:
            back.extend(x3(nback))

        print("back",back)
        print("")
    

def execute_bidir(orden, matriz, ini, end):
    if(orden > 2 or matriz > 4 or matriz < 3 or orden < 0):
        return "Valor ingresado incorrectamente"

    os.system("clear")  
    if(matriz == 3 and orden == 1):
        bidir_analysis(ini, end)

    elif(matriz == 3 and orden == 2):
        bidir_analysis(ini, end, False)

    elif(matriz == 4 and orden == 1):
        bidir_analysis(ini, end, True,False)

    else:
        bidir_analysis(ini, end, False,False)