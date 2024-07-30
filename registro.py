import cragar_guardar as gg

def regis_citi():
    data  = gg.cargar_ciudades()
    datos = {}
    cd_postal = int(input("Digite el codigo postal de la ciudad: "))
    if str(cd_postal) in data["ciudades"]:
        print("Ya hay una ciudad con este codigo postal")
    else:
        datos["Nombre"] = str(input("Digite el nombre de la ciudad: "))
        datos["Pais"] = str(input("Digite el Pais de la ciudad: "))
        datos["Poblacion"] = int(input("Digite la poblacion de la ciudad: "))
        data["ciudades"][cd_postal] = datos
        gg.guarda_ciudades(data)