import cragar_guardar as gg
def edit_citi():
    while True:
        data = gg.cargar_ciudades()
        cd_postal = int(input("Digite el codigo postal de la ciudad: "))
        if str(cd_postal) in data["ciudades"]:
            print("Que deseas editar de la ciudad")
            menu = ["1. Para nombre", "2. Para pais", "3. Para poblacion", "4. Para salir"]
            for n in menu:
                print(n)
            op  = int(input("Seleccione una opcion :"))
            if op == 1:
                nuevo = str(input("DIgite el nuevo nombre de la ciudad: "))
                data["ciudades"][str(cd_postal)]["Nombre"] = nuevo
                gg.guarda_ciudades(data)
                break
            elif op == 2:
                nuevo = str(input("DIgite el nuevo nombre del pais de la ciudad: "))
                data["ciudades"][str(cd_postal)]["Pais"] = nuevo
                gg.guarda_ciudades(data)
                break
            elif op == 3:
                nuevo = int(input("DIgite el nuevo numero de la poblacion: "))
                data["ciudades"][str(cd_postal)]["Poblacion"] = nuevo
                gg.guarda_ciudades(data)
                break
            elif op == 4:
                print("Saliendo...")
                break
            
        else:
            print("No hay ninguna ciudad con este codigo postal regitrela")

edit_citi()
        
    