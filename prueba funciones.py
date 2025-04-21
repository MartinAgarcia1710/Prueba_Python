def calcular_edad(anio_nacimiento):
    print("Calculando edad")
    return 2025 - anio_nacimiento


nac = int(input("Ingrese año de nacimiento"))

edad = calcular_edad(nac)

print(f"Tenes entre {edad - 1} y {edad} años")

def funcion_inservible():
    pass


