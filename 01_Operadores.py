# Operadores Aritméticos:

    # Suma y Resta
    1 + 2 = 3
    1 + 2 + 3 = 6
    1 - 2 + 3 = 2
    1 - (2 + 3) = -4

    # Cambio de Signo
    -3 = -3
    -(1 + 2) = -3
    --3 = 3

    # Multiplicación y División
    2 * 3 = 6
    3 / 2 = 1.5
    4 / 2 = 2.0
    3 * 4 / 2 = 6.0
    12 / 3 * 2 = 8.0

    # División Entera
    3 // 2 = 1
    4 // 2 = 2
    -3 // 2 = -2

    # Módulo o Resto
    27 % 5 = 2
    25 % 5 = 0

    # Exponenciación (es asociativa por la derecha)
    2 ** 3 = 8
    2 ** 3 ** 2 = 512


# Operadores Lógicos:

    # and
    True and True = True
    True and False = False
    False and True = False
    False and False = False

    # or
    True or True = True
    True or False = True
    False or True = True
    False or False = False

    # not (negación o no lógico)
    not True = False
    not False = True

    # Orden Operadores Lógicos (not, and, or)
    True or False and not False = True


# Operadores de Comparación

    # Igualdad ( == es igual que)
    2 == 3 = False
    2 == 2 = True
    2.1 == 2.1 = True
    True == True = True
    True == False = False
    2 == 1 + 1 = True
    (True or ( 2 == 1 + 2)) == True = True

    # Es distinto de ( != )
    1 != 0 = True
    1 != 1 = False

    # Es menor que ( < )
    2 < 1 = False
    1 < 2 = True

    # Es menor o igual que ( <= )
    -2 <= 2 = True

    # Es mayor que ( > )
    5 > 1 = True
    5 > 5 = False

    # Es mayor o igual que ( >= )
    5 >= 1 = True
    5 >= 5 = True

    # NOTA.- Sucesión de comparadores
    2 < 3 < 4 = True # La expresión se lee: (2 < 3) and (3 < 4)


# Orden Operadores ( **, cambio de signo, *, /, //, %, +, -, ==, !=, <, <=, >, >=, not, and, or)
    2 * 4 + 5 = 13
    2 + 4 * 5 = 22
    --2 * 2 = 4
    -3 // 2 = -2
    2 + 3 ** 2 * 5 = 47
    2 + (( 3 ** 2 ) * 5 ) = 47
    2 + 3 ** ( 2 * 5 ) = 59051
    -3 ** 2 = -9
    