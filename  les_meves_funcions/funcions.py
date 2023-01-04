from dades import *
# EJERCICIO 2
def new_tfn():
    # PRE: No recibe ningun parámetro. La función pide un numero de teléfono de 9 digitos, entero.
    # POST: La función devuelve un string con el teléfono validado.
    correct = False
    tfn = ""
    while not correct:
        try:
            tfn = input("Tfn: ")
            if not tfn.isdigit():
                raise ValueError("The tfn must to contain only numbers")
            elif len(tfn) != 9:
                raise ValueError("The tfn must to have 9 numbers")
            correct = True
        except ValueError as e:
            print(e)
    return tfn


# EJERCICIO 4
def new_item_id():
    # PRE: No recibe ningun parámetro. La función pide una ID de artículo que sea un entero, no usada, postiva.
    # POST: Devuelve una ID válida
    correct = False
    ID = 0
    list_ID = list(dict_articulos.keys())
    while not correct:
        try:
            ID = input("ID: ")
            if len(ID) == 0:
                raise ValueError("The ID must to be a number")
            if not ID.isdigit():
                if ID[0] == "-":
                    raise ValueError("The ID can't be negative")
                raise ValueError("The ID must to be a number")
            ID = int(ID)
            if ID in list_ID:
                raise ValueError("The ID is already in use")
            correct = True
        except ValueError as e:
            print(e)

    return ID

# EJERCICIO 5
def new_item_price():
    # PRE: No recibe ningun parámetro. La función pide una precio de artículo entero positvo.
    # POST: Devuelve una precio válido
    correct = False
    price = 0
    while not correct:
        try:
            price = input("Price: ")
            if len(price) == 0:
                raise ValueError("The ID must to be a number")
            if not price.isdigit():
                if price[0] == "-":
                    raise ValueError("The ID can't be negative")
                raise ValueError("The ID must to be a number")
            correct = True
            price = int(price)

        except ValueError as e:
            print(e)
    return price

# EJERCICIO 8
def find_item_id():
    # PRE: No recibe ningun parámetro. La función pide una ID de artículo entero positvo existente en el diccionario.
    # POST: Devuelve la ID
    correct = False
    ID = 0
    list_ID = list(dict_articulos.keys())
    while not correct:
        try:
            ID = input("ID: ")
            if len(ID) == 0:
                raise ValueError("The ID must to be a number")
            if not ID.isdigit():
                if ID[0] == "-":
                    raise ValueError("The ID can't be negative")
                raise ValueError("The ID must to be a number")
            ID = int(ID)
            if ID not in list_ID:
                raise ValueError("The ID don't exist")
            correct = True
        except ValueError as e:
            print(e)
    return ID

# EJERCICIO 10
def order_list(llista, ordre="des"):
    # PRE: llista con valores no definidos. orde, por defecto "des", ordena de forma desdecendente cuando ordre = des,
    #      y ordena crecientemente cuando ordre = asc
    # POST: Devuelve el parametro llista ordenada segun el parametro ordre
    try:
        if type(llista) != list:
            raise ValueError("The parameter llista must to be a list")
        if ordre not in ["des", "asc"]:
            raise TypeError("The ordre must to be des or asc")
        for i in range(1, len(llista)-1):
            if type(llista[i]) != type(llista[i-1]):
                raise TypeError("The list must to have the same variable type")

        # BUBBLE SORT
        for pasada in range(len(llista) - 1):
            lista_ordenada = True
            for i in range(len(llista) - 1 - pasada):

                if ordre == "des":
                    if llista[i] < llista[i + 1]:
                        lista_ordenada = False
                        aux = llista[i]
                        llista[i] = llista[i + 1]
                        llista[i + 1] = aux

                elif ordre == "asc":
                    if llista[i] > llista[i + 1]:
                        lista_ordenada = False
                        aux = llista[i]
                        llista[i] = llista[i + 1]
                        llista[i + 1] = aux

            if lista_ordenada:
                break

    except ValueError as e:
        print(e)
    except TypeError as e:
        print(e)
    return llista

# EJERCICIO 11
def ordre_dict_by_key(diccionar, ordre, key= ""):

