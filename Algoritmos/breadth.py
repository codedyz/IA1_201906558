import os
from successors import *

def BFS_analysis(queue, end, limit, orden=True, dimen=True):
    node_visited = 0 # Cantidad Nodos Visitados
    total_node = 1
    queue = [(node, 1) for node in queue]
    while len(queue) > 0:
        current, level = queue.pop(0) # Nodos visitados
        
        if(dimen == False):
            new_queue = x4(current)
        else:
            new_queue = x3(current)

        if(orden == False):
            new_queue = list(reversed(new_queue))

        queue += [(node, level + 1) for node in new_queue]

        node_visited += 1
        
        if (current == end):
            print("-> RESULTADOS")
            print("NODOS VISITADOS:", node_visited, "| NODOS TOTALES:",total_node, "| NODOS NO VISITADOS:", total_node-node_visited)
            break
        
        total_node += len(new_queue) 

        if level > limit:
            print("Limite de nivel alcanzado en modo", "ASCENDENTE" if orden else "DESCENDENTE")
            print("-> RESULTADOS")
            print("NODOS VISITADOS:", node_visited-1, "| NODOS TOTALES:", total_node, "| NODOS NO VISITADOS:", total_node - node_visited)
            break

        print(f"Nivel:{level:<4} NodoPadre:{current:<4} NivelPadre:{level-1:<8} {new_queue} {total_node}")
        

    
def execute_breadth(orden, matriz, ini, end, limit = 20):
    if(orden > 2 or matriz > 4 or matriz < 3 or orden < 0):
        return "Valor ingresado incorrectamente"

    os.system("clear")  
    if(matriz == 3 and orden == 1):
        queue = [ini]
        BFS_analysis(queue, end, limit)

    elif(matriz == 3 and orden == 2):
        queue = [ini]
        BFS_analysis(queue, end, limit, False)

    elif(matriz == 4 and orden == 1):
        queue = [ini]
        BFS_analysis(queue, end, limit, True,False)

    else:
        queue = [ini]
        BFS_analysis(queue, end, limit, False,False)

