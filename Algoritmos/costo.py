import os
from utils import *
def inc_generator():
    id = 1
    while True:
        yield id
        id += 1

id_gen = inc_generator()




def sucesores(n):
    graph = {
        'A': [('B', 2), ('C', 3), ('D', 4)],
        'B': [('C', 1), ('D', 3)],
        'C': [('B', 1), ('D', 2)],
    }

    return [[dest, n[1] + cost, next(id_gen),n[3]+1] for dest, cost in graph.get(n[0], [])]

def costo(start, end, orden=True, dimen=True):
    dot = 'graph G{\n'
    lista = [[start, 0, next(id_gen),0]]
    dot += f'{lista[0][2]} [label="{lista[0][0]} {lista[0][3]}"];\n'
    viajero_list = []
    while lista:
        current = lista.pop(0)
        if current[0] == end: 
            printscs(current)
            dot += f'{current[2]} [label="{current[0]} {current[3]}", fillcolor="green", style=filled];\n'

            dot += '}'
            #print(dot)
            break

        print(lista)
        printscs(current)

        viajero_list.append(current[0])
        print("SI DEBEN IR")

        temp = sucesores(current)
        print(" ",temp)
        for val in temp:
            dot += f'{val[2]} [label="{val[0]} {val[3]}"];\n{current[2]}--{val[2]} [xlabel="{val[1]}"];\n'


        lista = sorted(lista+ temp, key=lambda x: x[1])
        dot += "\n"
        print("")

    return dot

def execute_costo(ini, end):


    os.system("clear")  


    return costo(ini, end)
