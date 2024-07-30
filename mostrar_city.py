import cragar_guardar as gg

def mostrar_ciudad():
    data = gg.cargar_ciudades()
    cd_postal = int(input("Ingrese el codigo postal de la ciudad: ")) 
    if str(cd_postal) in data["ciudades"]:
        print("La ciudad ", data["ciudades"][str(cd_postal)]["Nombre"], "Con el codigo postal ", cd_postal, "que se encuentra en el pais", data["ciudades"][str(cd_postal)]["Pais"], "con la poblacion", data["ciudades"][str(cd_postal)]["Poblacion"] )
    
