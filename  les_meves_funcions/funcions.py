from dades import *

#Ex 1
def getOpt(textOpts="",inputOptText="",rangeList=[],dictionary={},exceptions=[]):
    correct = False
    opc = ''
    while not correct:
        print(textOpts)
        opc = input(inputOptText)
        if opc not in dictionary:
            try:
                opc = int(opc)
                if opc not in rangeList and opc not in exceptions:
                    raise TypeError('Incorrect Option')
                else:
                    correct = True
            except ValueError:
                print('Please, introduce only numbers')
                input(press)
            except TypeError as e:
                print(e)
                input(press)
        else:
            correct = True
    return opc

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

#Ex 3
def new_nif(new='yes'):
    correct = False
    newnif = ''
    while not correct:
        try:
            newnif = input('Introduce the new NIF: ')
            if not len(newnif) == 9:
                raise ValueError('Invalid NIF length')
            elif not newnif[:8].isdigit():
                raise ValueError('Invalid NIF numbers')
            elif not newnif[8].isalpha():
                raise ValueError('Invalid NIF letter')
            elif not letrasDni[int(newnif[:8]) % 23].casefold() == newnif[8].casefold():
                raise ValueError('Incorrect NIF letter')
            elif newnif.upper() in dict_clientes:
                if new == 'yes':
                    raise ValueError('That NIF already exists in the database')
            correct = True
        except ValueError as e:
            print(e)

    return newnif.upper()

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
                raise AssertionError("The ID must to be a number")
            if not ID.isdigit():
                if ID[0] == "-":
                    raise AssertionError("The ID can't be negative")
                raise AssertionError("The ID must to be a number")
            ID = int(ID)
            if ID in list_ID:
                raise AssertionError("The ID is already in use")
            correct = True
        except AssertionError as e:
            print(e)

    return ID

# EJERCICIO 5
def new_item_stock():
    # PRE: No recibe ningun parámetro. La función pide un stock de artículo que sea un entero y postivo.
    # POST: Devuelve un stock válido
    correct = False
    stock = 0
    while not correct:
        try:
            stock = input("Stock: ")
            if len(stock) == 0:
                raise AssertionError("The stock must to be a number")
            if not stock.isdigit():
                if stock[0] == "-":
                    raise AssertionError("The stock can't be negative")
                raise AssertionError("The stock must to be a number")
            stock = int(stock)
            correct = True
        except AssertionError as e:
            print(e)

    return stock

#Ex 6
def new_item_price():
    correct = False
    newprice = ''
    while not correct:
        try:
            newprice = int(input('New Price: '))
            if newprice < 0:
                raise AssertionError('Please, introduce a price above 0')
            correct = True
        except AssertionError as e:
            print(e)
            input(press)
        except ValueError:
            print('Please, introduce only numbers')
            input(press)

    return newprice

#Ex 7
def new_item_name():
    correct = False
    newname = ''
    while not correct:
        try:
            newname = input('New Name: ')
            if newname == ' ' * len(newname):
                raise ValueError("The name can't contain only spaces.")
            for i in dict_articulos:
                if dict_articulos[i]['nombre'].casefold() == newname.casefold():
                    raise ValueError('This item name already exists. Try another one')

            correct = True
        except ValueError as e:
            print(e)
            input(press)

    return newname

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

# EJERCICIO 9
def print_item(id,**values):
    # PRE:
    # POST:
    list_id = list(dict_articulos.keys())
    list_prop = list(dict_articulos[list_id[0]].keys())
    try:
        if id not in list_id:
            raise ValueError("The ID that you have introduce doesn't exist")
        for key in values:
            if key not in list_prop:
                raise ValueError("The key {} doesn't exist in the dictionary".format(key))
        if len(values) == 0:
            mostrar = "ID".ljust(15) + " "*5 + str(id).rjust(30) + "\n"
            mostrar += "Name".ljust(15) + " "*5 + dict_articulos[id]["nombre"].rjust(30) + "\n"
            mostrar += "Stock".ljust(15) + " "*5 + str(dict_articulos[id]["stock"]).rjust(30) + "\n"
            mostrar += "Price".ljust(15) + " " *5 + str(dict_articulos[id]["precio"]).rjust(30)
        else:
            mostrar = "ID".ljust(15) + " " * 5 + str(id).rjust(30) + "\n"
            if "nombre" in values:
                mostrar += "Name".ljust(15) + " " * 5 + values["nombre"].rjust(30) + "\n"
            else:
                mostrar += "Name".ljust(15) + " " * 5 + dict_articulos[id]["nombre"].rjust(30) + "\n"
            if "stock" in values:
                mostrar += "Stock".ljust(15) + " " * 5 + str(values["stock"]).rjust(30) + "\n"
            else:
                mostrar += "Stock".ljust(15) + " " * 5 + str(dict_articulos[id]["stock"]).rjust(30) + "\n"
            if "precio" in values:
                mostrar += "Price".ljust(15) + " " * 5 + str(values["precio"]).rjust(30)
            else:
                mostrar += "Price".ljust(15) + " " * 5 + str(dict_articulos[id]["precio"]).rjust(30)
        print(mostrar)

    except ValueError as e:
        print(e)


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

print_item(34, stock="Pablo")