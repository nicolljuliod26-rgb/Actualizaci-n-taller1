from colorama import init, Fore, back,style
import os #intersctua con el sistema operativo (archivo, directorio, rutas, variables de entorno).
import sys # Maneja la configuracion y el entorno del interprete de python(argumentos de linea de comando,
#  rutas de modulo)
import subprocess # ejecuta comandos externos y programas, controlando entrada/salida)

init(autoreset=True)

while True:
    #Encabezado
    print(Fore.GREEN+"=======================================")
    print("taller 1 - algoritmos basicos de pyt7hon")
    print("by Nicoll Julio Delgado")
    print("Menu principal")
    print("======================================")

    for i in range(1,26):
        print(f"ejecutar algoritmo{i}")
        print("0.salir\n")
        # 1. ejecutar algoritmo 1
        # 2. ejecutar algoritmo 2
        opcion = input("selecciona una opcion:")
        
        if opcion == "0":
            print("saliendo...")
            break

        if opcion.isdigit() and 1<= int(opcion) <=25:
          archivo= f"a {opcion}.py"

        if os.path.exists(archivo):
            subprocess.run([sys.executable, archivo])
        else:
            print(f"No existe {archivo}")
    else:
        print("opcion invalida.")



        input("\n  presiona enter para continuar") 
    
        
    

    #
    input("presiona enter para continuar...")