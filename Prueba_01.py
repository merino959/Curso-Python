print("comienzo")
palabra = "ordenador"
tupalabra = ""
vidas = 5

while vidas > 0:
    fallas = 0

    for letra in palabra:
        if letra in tupalabra:
            print(letra, end="")
        else:
            print("*", end="")
            fallas += 1

    if fallas == 0:
        print("")
        print("Ganaste.")
        break
    print("")
    tuletra = input("Introduce una letra:")
    tupalabra += tuletra
    print(tupalabra)
    if tuletra not in palabra:
        vidas -= 1
        print("Equivocacion.")
        print("Tu tienes ", vidas, " vidas.")
    if vidas == 0:
        print("Perdiste.")
else:
    print("Gracias por jugar.")
