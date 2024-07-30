import letreros

print("Bienvenido a consultar paises")
print("Ingrese su Nombre usuario")
Nombre=input("-")
print("Bienvenido",Nombre)


while True:
    print("""
          1. Crear cuidades
          2. Ediar Cuidades
          3. Mostrar Cuidades
          4. Buscar Cuidades
          5. Salir""")
    opc=input("-")
    if opc == 1:
        letreros.letrero1()
    elif opc == 2:
        letreros.letrero2()
    elif opc == 3:
        letreros.letrero3()
    elif opc == 4 :
        letreros.letrero4()
    elif opc == 5:
        letreros.letrero5()
        break
    else:
        print("Opcion no validaa")
        