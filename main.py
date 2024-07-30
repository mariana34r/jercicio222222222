import letreros
import registro
import editar_city
import mostrar_city

print("Binevenido :)")
print("Ingrese su Nombre Usuario")
Nombre=input("-")
print("Binevenido",Nombre)
while True:
    print("Que desea hacer ")
    print("\n.1 Crear cuidades\n2.Editar Cuidades\n3.Mostrar Cuidades\n4.Salir")
    print("Escoga una Opcion")
    try:
        opc = input("-")
        if opc == '1':
            letreros.letrero1()
            registro.regis_citi()
        elif opc == '2':
            letreros.letrero2()
            editar_city.edit_citi()
        elif opc == '3':
            letreros.letrero3()
            mostrar_city.mostrar_ciudad() 
        elif opc == '4':
            letreros.letrero5()
            break  
        else:
            print("Opción no válida. Por favor, ingrese un número entre 1 y 5.")
    
    except Exception as e:
        
        print(f"Se ha producido un error: {e}")
        print("HOLA MUNDO..")
        
        
print("devuelvanmelo")