# Profundidad, Eddy Diaz, 2S2024
import os
from successors import *

def DFS_analysis(stack, end, limit,  orden=True, dimen=True):
    node_visited = 0  # Cantidad Nodos Visitados
    total_node = 1
    stack = [(node, 1) for node in stack]
    while len(stack) > 0:
        current, level = stack.pop()  # Nodos visitados
        new_stack = x3(current)

        if dimen == False:
            new_stack = x4(current)

        if orden == False:
            new_stack = list(reversed(new_stack))

        # Añadir los nodos en orden inverso al stack
        stack.extend([(node, level + 1) for node in reversed(new_stack)])

        print(f"Nivel:{level:<4} NodoPadre:{current:<4} NivelPadre:{level-1:<8} {new_stack}")
        node_visited += 1

        if current == end:
            print("-> RESULTADOS")
            print("NODOS VISITADOS:", node_visited, "| NODOS TOTALES:",total_node, "| NODOS NO VISITADOS:", total_node-node_visited)
            break


        if level > limit:
            print("Limite de nivel alcanzado en modo", "ASCENDENTE" if orden else "DESCENDENTE")
            print("-> RESULTADOS")
            print("NODOS VISITADOS:", node_visited, "| NODOS TOTALES:", total_node, "| NODOS NO VISITADOS:", total_node - node_visited)
            break


        total_node += len(new_stack) 


def execute_depth(orden, matriz, ini, end, limit = 20):
    if(orden > 2 or matriz > 4 or matriz < 3 or orden < 0):
        return "Valor ingresado incorrectamente"

    os.system("clear")

    if(matriz == 3 and orden == 1):
        queue = [ini]
        DFS_analysis(queue, end, limit)

    elif(matriz == 3 and orden == 2):
        queue = [ini]
        DFS_analysis(queue, end, limit, False)

    elif(matriz == 4 and orden == 1):
        queue = [ini]
        DFS_analysis(queue, end, limit, True, False)

    else:
        queue = [ini]
        DFS_analysis(queue, end, limit, False,False)

