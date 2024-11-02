import os
from utils import printscs
from breadth import execute_breadth
from depth import execute_depth
from bidir import execute_bidir
from costo import execute_costo
from bf_cfl import bestfirst

def mostrar_menu():
    printscs("ALGORITMOS IA")
    print(" 1. Anchura")
    print(" 2. Anchura Limited")
    print(" 3. Profundidad")
    print(" 4. Profundidad Limited")
    print(" 5. Bidireccional")
    print(" 6. Costo Uniforme")
    print(" 7. Best First")
    print(" 8. Colinas")

    print(" 0. Salir")

def submenu1():
    while True:
        try:
            print("1. Ascendente")
            print("2. Descendente")
            orden = int(input("> "))

            print("3. 3x3")
            print("4. 4x4")
            matriz = int(input("> "))

            print("Ingrese estado inicial")
            ini = int(input("> "))

            print("Ingrese estado final")
            end = int(input("> "))
            return orden, matriz, ini, end
        except ValueError:
            os.system("clear")
            print("Error: Debes ingresar un número entero")

def submenu2():
    while True:
        try:
            print("Ingrese estado inicial")
            ini = str(input("> "))

            print("Ingrese estado final")
            end = str(input("> "))
            return ini, end
        except ValueError:
            os.system("clear")
            print("Error: Debes ingresar un string como estado")

def ejecutar_menu():
    while True:
        mostrar_menu()
        opcion = input(" > ")
        os.system("clear")
        if opcion == "1":
            printscs("Breadth Search")
            orden, matriz, ini, end = submenu1()
            execute_breadth(orden, matriz, ini, end)

        elif opcion == "2":
            printscs("Breadth Search Limited")
            orden, matriz, ini, end = submenu1()
            print("Ingrese limite de nivel")
            limit = int(input("> "))
            execute_breadth(orden, matriz, ini, end, limit)

        elif opcion == "3":
            printscs("Depth Search")
            orden, matriz, ini, end = submenu1()
            execute_depth(orden, matriz, ini, end)

        elif opcion == "4":
            printscs("Limited Depth Search")
            orden, matriz, ini, end = submenu1()
            print("Ingrese limite de nivel")
            limit = int(input("> "))
            execute_depth(orden, matriz, ini, end, limit)

        elif opcion == "5":
            printscs("Bidireccional")
            orden, matriz, ini, end = submenu1()
            execute_bidir(orden, matriz, ini, end)

        elif opcion == "6":
            printscs("Costo Uniforme")
            ini, end = submenu2()
            graph = execute_costo(ini, end)
            graph_in = input("Ingrese 1 si quiere imprimir el DOT")
            if(int(graph_in) == 1):
                os.system("clear")
                print(graph)

        elif opcion == "7":
            printscs("Best First")

            print("1. Casillas Fuera de Lugar")
            print("2. Manhattan")
            h = int(input("Ingrese heuristica:\n"))
            ini = str(input("Estado inicial:\n"))
            fin = str(input("Estado final:\n"))

            graph = bestfirst(ini.lower(), fin.lower(),h)

            graph_in = input("Ingrese 1 si quiere imprimir el DOT")
            if(int(graph_in) == 1):
                os.system("clear")
                print(graph)
            
        elif opcion == "8":
            printscs("Colinas")

            print("1. Casillas Fuera de Lugar")
            print("2. Manhattan")
            h = int(input("Ingrese heuristica:\n"))
            ini = str(input("Estado inicial:\n"))
            fin = str(input("Estado final:\n"))

            graph = bestfirst(ini.lower(), fin.lower(),h, True)

            graph_in = input("Ingrese 1 si quiere imprimir el DOT")
            if(int(graph_in) == 1):
                os.system("clear")
                print(graph)

        elif opcion == "0":
            exit()
        else:
            print("Opción no válida, intenta nuevamente.")
        input("Presiona Enter para continuar")
        os.system("clear")
        

# Ejecutar el menú
if __name__ == "__main__":
    os.system("clear")
    ejecutar_menu()