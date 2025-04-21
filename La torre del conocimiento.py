print("Bienvenidos a La torre del conocimiento")

print("para llegar a la cima, debes responder 4 preguntas correctamente")
respuestas_correctas = 0
piso_actual = 1

for piso in range(4):
    
    if piso_actual == 1:
        respuesta_correcta = "f"
        pregunta = "El mes de febrero siempre tiene la misma cantidad de dias"

    elif piso_actual == 2:
        respuesta_correcta = "f"
        pregunta = "Estamos en una clase de ingles"
    elif piso_actual == 3:
        respuesta_correcta ="f"
        pregunta = "Messi es un poeta argentino"
    else:
        respuesta_correcta = "v"
        pregunta = "Hoy es viernes"
            
    print(pregunta)

    while True:
        respuesta = input("Ingrese respuesta: ")

        if respuesta == "v" or respuesta == "f":
            if respuesta == respuesta_correcta:
                print("Respuesta correcta")
                piso_actual += 1
                respuestas_correctas += 1
                break
            else:
                print("Respuesta incorrecta")
        else:
            print("Letra ingresada es incorrecta")

print("Felicitaciones, llegaste al piso 5\nJuego Terminado")
print("Game over")