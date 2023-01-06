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
            raise TypeError("The parameter ordre must to be des or asc")
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
def ordre_dict_by_key(diccionari, ordre, key= ""):
    # PRE: el parámetro diccionari contiene un diccionario, el parámetro ordre solo puede ser o "des" o "asc",
    #      el último parámetro por defecto vale "", este se usará en el caso que el diccionario contenga otros
    #      diccionarios y querramos ordenar por un subdiccionario en concreto, pasando su key.
    valores = []
    list_clau = []
    try:
        if type(diccionari) != dict:
            raise TypeError("The parameter diccionari must be a dictionary")

        list_clau = list(diccionari.keys())

        # Averiguamos si diccionari es del tipo 1, un diccionario con valores simples, o del tipo 2, diccionario de
        # diccionarios
        dict_type = 2
        for i in diccionari:
            if type(diccionari[i]) != dict:
                dict_type = 1

        if key != "" and dict_type == 1:
            raise TypeError("You can't introduce a key with a simple dictionary")

        if key == "" and dict_type == 2:
            raise TypeError("You must introduce a key if you introduce a dictionary of dictionaries")

        if ordre not in ["des", "asc"]:
            raise TypeError("The parameter ordre must to be des or asc")

        if dict_type == 2:
            list_key = list(diccionari[list_clau[0]].keys())
            if key not in list_key:
                raise TypeError("The key that have you introduce doesn't exist in the dictionary")
            for i in list_clau:
                valores.append(diccionari[i][key])
        else:
            for i in list_clau:
                valores.append(diccionari[i])

        for i in range(1, len(valores)-1):
            if type(valores[i]) != type(valores[i-1]):
                raise TypeError("The items that you are trying to sort are diferent types")

        if dict_type == 1:
            for pasada in range(len(list_clau) - 1):
                lista_ordenada = True
                for i in range(len(list_clau) - 1 - pasada):

                    if ordre == "des":
                        if diccionari[list_clau[i]] < diccionari[list_clau[i + 1]]:
                            lista_ordenada = False
                            aux = list_clau[i]
                            list_clau[i] = list_clau[i + 1]
                            list_clau[i + 1] = aux

                    elif ordre == "asc":
                        if diccionari[list_clau[i]] > diccionari[list_clau[i + 1]]:
                            lista_ordenada = False
                            aux = list_clau[i]
                            list_clau[i] = list_clau[i + 1]
                            list_clau[i + 1] = aux
                if lista_ordenada:
                    break
        else:
            for pasada in range(len(list_clau) - 1):
                lista_ordenada = True
                for i in range(len(list_clau) - 1 - pasada):

                    if ordre == "des":
                        if diccionari[list_clau[i]][key] < diccionari[list_clau[i + 1]][key]:
                            lista_ordenada = False
                            aux = list_clau[i]
                            list_clau[i] = list_clau[i + 1]
                            list_clau[i + 1] = aux

                    elif ordre == "asc":
                        if diccionari[list_clau[i]][key] > diccionari[list_clau[i + 1]][key]:
                            lista_ordenada = False
                            aux = list_clau[i]
                            list_clau[i] = list_clau[i + 1]
                            list_clau[i + 1] = aux

                if lista_ordenada:
                    break
    except TypeError as e:
        print(e)

    return list_clau


