from Problema1 import duplicar_los_numeros
from Problema2 import filtrar_palabras_largas
from Problema3 import ordenar_lista_duplas
from Problema4 import cuadrado
from Problema5 import filtrar_numeros_impares


def main():
    print("Selecciona el problema que deseas ejecutar:")
    print("1. Problema 1")
    print("2. Problema 2")
    print("3. Problema 3")
    print("4. Problema 4")
    print("5. Problema 5")

    opcion = int(input("Ingresa el número del problema: "))

    if opcion == 1:
        duplicar_los_numeros.problema1()
    elif opcion == 2:
        filtrar_palabras_largas.problema2()
    elif opcion == 3:
        ordenar_lista_duplas.problema3()
    elif opcion == 4:
        cuadrado.problema4()
    elif opcion == 5:
        filtrar_numeros_impares.problema5()
    else:
        print("Opción no válida")

if __name__ == "__main__":
    main()
