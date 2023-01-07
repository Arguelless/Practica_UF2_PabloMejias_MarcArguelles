from les_meves_funcions.dades import *
from les_meves_funcions.funcions import *

salir = False

menu00 = True

menu1 = False
menu12 = False
menu13 = False
menu14 = False

menu2 = False
menu22 = False

menu3 = False
menu32 = False
menu321 = False

while not salir:
    while menu00:
        option = getOpt(main, flecha, [1, 2, 3, 4])
        if option == 1:
            menu1 = True
            menu00 = False
        elif option == 2:
            menu2 = True
            menu00 = False
        elif option == 3:
            menu3 = True
            menu00 = False
        elif option == 4:
            input('Closing program. Press enter to Exit.')
            salir = True
            menu00 = False


    while menu1:

        option = getOpt(itemmenu, flecha, [1, 2, 3, 4, 5])

        if option == 1:
            error = True
            newid = new_item_id()
            newname = new_item_name()
            newstock = new_item_stock()
            newprice = new_item_price()
            print('ID: {}\nName: {}\nStock: {}\nPrice: {}\nSave new Item? Y/y = Yes.'.format(newid, newname, newstock, newprice))
            answer = input('Answer: ')
            if answer.casefold() == 'y':
                print('Item saved!!')
                dict_articulos[newid] = {"nombre": newname, "stock": newstock, "precio": newprice}
            else:
                print('Item not saved')

            input(press)

        elif option == 2:
            menu12 = True
            menu1 = False
        elif option == 3:
            menu13 = True
            menu1 = False
        elif option == 4:
            menu14 = True
            menu1 = False
        elif option == 5:
            menu1 = False
            menu00 = True

    while menu12:
        idtomodify = find_item_id()
        print("You want to modify the item:")
        print_item(idtomodify)
        input(press)

        buclemodify = True
        while buclemodify:
            option = getOpt(menumodify, 'What do you want to modify: ', [1, 2, 3, 4, 5, 6])

            if option == 1:
                newname = new_item_name()
                print_item(idtomodify, nombre=newname)
                answer = input("Save the item as? Y/y = yes: ")

                if answer.casefold() == 'y':
                    dict_articulos[idtomodify]['nombre'] = newname

            elif option == 2:
                newstock = new_item_stock()
                print_item(idtomodify, stock=newstock)
                answer = input("Save the item as? Y/y = yes: ")
                if answer.casefold() == 'y':
                    dict_articulos[idtomodify]['stock'] = newstock

            elif option == 3:
                newprice = new_item_price()
                print_item(idtomodify, precio=newprice)
                answer = input("Save the item as? Y/y = yes: ")
                if answer.casefold() == 'y':
                    dict_articulos[idtomodify]['precio'] = newprice

            elif option == 4:
                print_item(idtomodify)
                input(press)

            elif option == 5:
                menu12 = False
                menu00 = True
                buclemodify = False

            elif option == 6:
                menu12 = False
                menu1 = True
                buclemodify = False

    while menu13:
        option = getOpt(menufinditem, flecha, [1, 2, 3, 4])

        if option == 1:
            itemid = find_item_id()

            if itemid in dict_articulos:
                print(cabecerafinditem + str(itemid).rjust(4) + ' ' + dict_articulos[itemid].get('nombre').ljust(40) +
                      ' ' + str(dict_articulos[itemid].get('stock')).rjust(8) + ' ' +
                      str(dict_articulos[itemid].get('precio')).rjust(8) + '\n')
            else:
                print(cabecerafinditem, 'There are no items with that ID.\n', sep="", end="")

            input(press)

        elif option == 2:
            itemname = input('What to look for: ')
            cadena = str()
            for idd in dict_articulos:
                if itemname.casefold() in dict_articulos[idd].get('nombre').casefold():
                    cadena += (str(idd).rjust(4) + '  ' + dict_articulos[idd].get('nombre').ljust(40)
                               + ' ' + str(dict_articulos[idd].get('stock')).rjust(8) + ' ' +
                               str(dict_articulos[idd].get('precio')).rjust(8) + '\n')
            if cadena == str():
                print('There are no items with that name')
            else:
                print(cabecerafinditem + cadena)
            input(press)

        elif option == 3:
            menu13 = False
            menu00 = True
        elif option == 4:
            menu13 = False
            menu1 = True

    while menu14:
        option = getOpt(menulistitem, flecha, [1, 2, 3, 4, 5, 6, 7])
        cadena = str()
        if option == 1:
            llista = list(dict_articulos)
            llista = order_list(llista, "asc")
            for idd in llista:
                cadena += (str(idd).rjust(4) + '  ' + dict_articulos[idd].get('nombre').ljust(40)
                           + ' ' + str(dict_articulos[idd].get('stock')).rjust(8) + ' ' +
                           str(dict_articulos[idd].get('precio')).rjust(8) + '\n')
            print(cabecerafinditem + cadena)
            input(press)

        elif option == 2:
            llista = ordre_dict_by_key(dict_articulos, "asc", "nombre")

            for idd in llista:
                cadena += (str(idd).rjust(4) + '  ' + dict_articulos[idd].get('nombre').ljust(40)
                           + ' ' + str(dict_articulos[idd].get('stock')).rjust(8) + ' ' +
                           str(dict_articulos[idd].get('precio')).rjust(8) + '\n')
            print(cabecerafinditem + cadena)
            input(press)

        elif option == 3:
            llista = ordre_dict_by_key(dict_articulos, "asc", "stock")

            for idd in llista:
                cadena += (str(idd).rjust(4) + '  ' + dict_articulos[idd].get('nombre').ljust(40)
                           + ' ' + str(dict_articulos[idd].get('stock')).rjust(8) + ' ' +
                           str(dict_articulos[idd].get('precio')).rjust(8) + '\n')
            print(cabecerafinditem + cadena)
            input(press)

        elif option == 4:
            contador = {}
            for i in dict_compras:
                for j in dict_compras[i]['articulos']:
                    if j in contador:
                        contador[j] += dict_compras[i]['articulos'][j]
                    else:
                        contador[j] = dict_compras[i]['articulos'][j]

            llista = ordre_dict_by_key(contador, "des")

            for idd in llista[:3]:
                cadena += (str(idd).rjust(4) + '  ' + dict_articulos[idd].get('nombre').ljust(40)
                           + ' ' + str(dict_articulos[idd].get('stock')).rjust(8) + ' ' +
                           str(dict_articulos[idd].get('precio')).rjust(8) + '  ' + str(contador.get(idd)).rjust(10) + '\n')
            print(bestitems + cadena)
            input(press)

        elif option == 5:
            contador = {}
            for i in dict_compras:
                for j in dict_compras[i]['articulos']:
                    if j in contador:
                        contador[j] += dict_compras[i]['articulos'][j]
                    else:
                        contador[j] = dict_compras[i]['articulos'][j]

            llista = ordre_dict_by_key(contador, "asc")
            for idd in llista[:3]:
                cadena += (str(idd).rjust(4) + '  ' + dict_articulos[idd].get('nombre').ljust(40)
                           + ' ' + str(dict_articulos[idd].get('stock')).rjust(8) + ' ' +
                           str(dict_articulos[idd].get('precio')).rjust(8) + '  ' + str(contador.get(idd)).rjust(10) + '\n')
            print(worstitems + cadena)
            input(press)

        elif option == 6:
            menu14 = False
            menu00 = True
        elif option == 7:
            menu14 = False
            menu1 = True


    while menu2:
        option = getOpt(purchasemenu, flecha, [1, 2, 3, 4])

        if option == 1:
            # OPCION 1 (NO IMPLEMENTADA)
            print("Find purchase")
        elif option == 2:
            # NOS REDIRIGE AL MENU22
            menu2 = False
            menu22 = True
        elif option == 3:
            # OPCION 3 (NO IMPLEMENTADA)
            print("New purchase")
        elif option == 4:
            # VOLVEMOS AL MENUMAIN
            menu00 = True
            menu2 = False

    while menu22:
        option = getOpt(menuListPurchase, flecha, [1, 2, 3, 4])

        if option == 1:
            print(cabeceraListAll)
            #RECORREMOS EL DICCIONARIO compra_cliente
            for id_compra in compra_cliente:
                #GUARDAMOS EL TOTAL DE DINERO GASTADO EN LA COMPRA EN LA VARIABLE total
                total = 0
                #ITERAMOS LOS ARTICULOS DE LA COMPRA
                for j in dict_compras[id_compra]["articulos"]:
                    #SUMAMOS EL VALOR DEL ARTICULO * LA CANTIDAD
                    total += dict_articulos[j]["precio"] * dict_compras[id_compra]["articulos"][j]
                #CREAMOS LA LINEA QUE MUESTRA LA ID, EL CLIENTE, LA FECHA Y EL TOTAL GASTADO
                seq = id_compra.ljust(11) + " "*10 + dict_clientes[compra_cliente[id_compra]]["nombre"].ljust(25) + " "*7
                seq += str(dict_compras[id_compra]["fecha"]).rjust(8) + " "*8 + str(total).rjust(15)

                print(seq)
            print()
            input(press)

        elif option == 2:
            # CREAMOS UNA LISTA CON TODAS LAS ID'S DE LOS ARTICULOS
            ID_list = list(dict_articulos.keys())
            option = find_item_id()

            # ITERAMOS TODAS LAS COMPRAS
            for id_compra in dict_compras:
                #Creamos una lista con todas las ID's de los articulos de la compra
                lista_aux = list(dict_compras[id_compra]["articulos"].keys())
                #COMPROBAMOS SI LA ID INTRODUCIDA (option) ESTA EN LA COMPRA
                if option in lista_aux:
                    print(cabeceraListCont)
                    seq = id_compra.ljust(5) + " "*5 + dict_clientes[compra_cliente[id_compra]]["nombre"].ljust(18)
                    seq += " "*5
                    primero = True
                    total = 0
                    # ITERAMOS LA CANTIDAD DE ARTICULOS DE LA COMPRA
                    for articulo in dict_compras[id_compra]["articulos"]:
                        # SI ES EL PRIMER ARTICULO DE LA COMPRA TENDRA UNA JUSTIFICACIÓN DISTINTA POR ESO LO SEPARAMOS
                        if primero:
                            total += dict_articulos[articulo]["precio"] * dict_compras[id_compra]["articulos"][articulo]
                            primero = False
                            seq += str(articulo).rjust(7) + " "*2 + dict_articulos[articulo]["nombre"].ljust(30)
                            seq += " "*5 + str(dict_compras[id_compra]["articulos"][articulo]).rjust(6)
                            seq += " "*5 + str(dict_articulos[articulo]["precio"]).rjust(5) +"\n"
                        else:
                            total += dict_articulos[articulo]["precio"] * dict_compras[id_compra]["articulos"][articulo]
                            seq += str(articulo).rjust(40) + " " * 2 + dict_articulos[articulo]["nombre"].ljust(30)
                            seq += " " * 5 + str(dict_compras[id_compra]["articulos"][articulo]).rjust(6)
                            seq += " " * 5 + str(dict_articulos[articulo]["precio"]).rjust(5) +"\n"
                    seq += "-"*93 + "\n" + "TOTAL" + str(total).rjust(88) + "\n"
                    print(seq)
            input(press)

        elif option == 3:
            menu22 = False
            menu2 = True

        elif option == 4:
            menu22 = False
            menu00 = True


    while menu3:
        option = getOpt(customermenu, flecha, [1, 2, 3])

        if option == 1:
            # CREAMOS NUEVO CLIENTE
            print(capNewCust)
            error = True
            DNI = ""
            NAME = ""
            TELF = ""

            # COMPROBAMOS EL DNI
            # CREAMOS UNA LISTA DE DNI's
            list_DNI = list(dict_clientes.keys())
            while error:
                DNI = input("Enter new NIF:")
                if len(DNI) != 9:
                    print("Incorrect length\n")
                    input(press)
                elif not DNI[:8].isdigit():
                    print("The first 8 characters of DNI are numbers\n")
                    input(press)
                elif not DNI[8].isalpha():
                    print("Dni has to end with a letter\n")
                    input(press)
                elif not letrasDni[int(DNI[:8]) % 23].casefold() == DNI[8].casefold():
                    print("Incorrect DNI letter\n")
                    input(press)
                elif DNI.upper() in list_DNI:
                    print("There is already a client with that NIF\n")
                    input(press)
                else:
                    print("DNI is correct\n")
                    error = False
                    input(press)
            error = True

            # COMPROBAMOS EL NOMBRE
            while error:
                NAME = input("Name of the new customer:")
                if not NAME.isalpha():
                    print("Incorrect name")
                else:
                    error = False
            error = True

            # COMPROBAMOS TELF
            while error:
                TELF = input("Tfn of the new customer:")
                if not TELF.isdigit():
                    print("The Tfn character are numbers")
                elif len(TELF) != 9:
                    print("The length of the Tfn is 9")
                else:
                    error = False
            error = True

            # MOSTRAMOS MENSAJE DE LOS DATOS INTRODUCIDOS
            print("Do you want to create the new customer? Y/y=yes:")
            seq = "NIF".ljust(5) + " " * 5 + DNI.rjust(12) + "\n" + "Name".ljust(5) + " " * 5 + NAME.rjust(
                12) + "\n" + "Tfn".ljust(5) + " " * 5 + TELF.rjust(12) + "\n"
            print(seq)

            # COMPROBAMOS LA RESPUESTA
            option = input("Answer:")
            if option in ["Y", "y", "yes"]:
                # CREAMOS UN DICCIONARIO AUXILIAR Y ACTUALIZAMOS EL DICC CLIENTES
                dict_aux = {DNI: {"nombre": NAME, "telefono": TELF}}
                dict_clientes.update(dict_aux)
                print("New client created")


        elif option == 2:
            # VAMOS AL MENU 32
            menu3 = False
            menu32 = True
        elif option == 3:
            # VOLVEMOS AL MAIN MENU
            input('Going back to Main Menu. Press Enter.')
            menu3 = False
            menu00 = True


    while menu32:
        option = getOpt(menuCustFind, flecha, [1, 2, 3, 4, 5])
        if option == 1:
            #BUSCAMOS POR DNI
            error = True
            # CREAMOS UNA LISTA DE DNI's
            list_DNI = list(dict_clientes.keys())
            #COMPROBAMOS EL DNI
            while error:
                DNI = input("NIF to find:")
                input(press)
                if len(DNI) != 9:
                    print("Incorrect length\n")
                    input(press)
                elif not DNI[:8].isdigit():
                    print("The first 8 characters of DNI are numbers\n")
                    input(press)
                elif not DNI[8].isalpha():
                    print("Dni has to end with a letter\n")
                    input(press)
                elif not letrasDni[int(DNI[:8])%23].casefold() == DNI[8].casefold():
                    print("Incorrect DNI letter\n")
                    input(press)
                elif DNI not in list_DNI:
                    error = False
                    print("There is not customer with dni", DNI)
                else:
                    #MOSTRAMOS LOS DATOS DE LA PERSONA
                    error = False
                    seq = "\n" + "NIF".ljust(5) + " "*5 + DNI.rjust(20) + "\n"
                    seq += "Name".ljust(5) + " "*5 + dict_clientes[DNI]["nombre"].rjust(20) + "\n"
                    seq += "Tfn".ljust(5) + " "*5 + dict_clientes[DNI]["telefono"].rjust(20) + "\n"
                    DNI_glob = DNI
                    print(seq)
                    input(press)
                    #NOS VAMOS AL MENU 321
                    menu32 = False
                    menu321 = True
        elif option == 2:
            #CABECERA
            cabName = "NIF".ljust(10) + " "*10 + "Name".ljust(19) + " " + "TFN".ljust(9) + "\n" + "="*49 + '\n'

            search = input("Name to search:")
            seq = cabName
            #VARIABLE PARA SABER SI NO HAY CONCIDENCIAS Y LA TABLA ESTÁ VACÍA
            Vacio = True
            encontrado = False
            #RECORREMOS TODOS LOS DNI'S
            for DNI in dict_clientes:
                #GUARDAMOS EL NOMBRE DEL CLIENTE EN UNA VARIABLE
                nombre = dict_clientes[DNI]["nombre"].casefold()
                #COMPROBAMOS QUE LOS CARACTERES INTRODUCIDOS POR EL USER CONCUERDAN CON ALGUN NOMBRE DEL DICCIONARIO
                if search.casefold() in nombre:
                    #SI ALGUN CARACTER NO COINIDE DESCARTAMOS AL CLIENTE
                    seq += DNI.ljust(10) + " "*10 + dict_clientes[DNI]["nombre"].ljust(19) + " " + dict_clientes[DNI]["telefono"].ljust(9) + '\n'
                    encontrado = True
            if encontrado:
                #SI NINGUN CARACTER HA HECHO SALTAR EL ERROR MOSTRAMOS SU NOMBRE EN LA TABLA
                Vacio = False
                print(seq)
            #MENSAJE CUANDO NO HAY NINGUNA COINCIDENCIA
            if Vacio:
                print("There is no name containing", search)
            input(press)

        elif option == 3:
            cabTop = "Customer".ljust(18) + " "*2 + "NIF".ljust(9) + " "*5 + "Total Purchases".rjust(26) + "\n" + "="*60
            print(cabTop)
            #COMPROBAMOS QUE EL DICCIONARIO NO ESTA VACÍO
            if len(dict_clientes) == 0:
                print("There is no customer registered")
            else:
                #CREAMOS UNA LISTA CON LOS DNI'S DE LOS CLIENTES QUE HECHO ALGUNA COMPRA
                list_DNI = list(cliente_compra.keys())
                #CREAMOS UN DICCIONARIO RELACIONANDO DNI Y NUM TOTAL DE COMPRAS
                dict_total = {}
                for dni in list_DNI:
                    #SUMAMOS EL TOTAL DE DINERO GASTADO ENTRE TODAS LAS COMPRAS DE UN CLIENTE
                    total = 0
                    for id_compra in cliente_compra[dni]:
                        for id_articulo in dict_compras[id_compra]["articulos"]:
                            total += dict_articulos[id_articulo]["precio"] * dict_compras[id_compra]["articulos"][id_articulo]

                    #ACTUALIZAMOS EL DICCIONARIO
                    dict_total.update({dni: total})

                llista = ordre_dict_by_key(dict_total, "des")
                #RECORREMOS LOS 3 PRIMEROS PUESTOS DE LA LISTA YA QUE SON (POR ORDEN) LOS QUE MAS HAN GASTADO
                for DNI in llista[:3]:
                    seq = dict_clientes[DNI]["nombre"].ljust(18) + " "*2 + DNI.ljust(9) + " "*5 + str(dict_total[DNI]).rjust(26)
                    print(seq)
            print()
            input(press)

        elif option == 4:
            #VOLVEMOS AL MAIN MENU
            menu32 = False
            menu00 = True
        elif option == 5:
            #VOLVEMOS AL MENU 32
            menu32 = False
            menu3 = True


    while menu321:
        #CABECERA PURCHASES
        capPurch = "\n" + "ID Purchase".ljust(11) + " "*4 + "Date".ljust(8) + " "*4 + "Total Purchase".rjust(18) + "\n" + "="*45

        #CABECERA DETAILED PURCHASES
        capDetPurch = "\n" + "ID".ljust(5) + " "*5 + "Date".ljust(8) + " "*4 + "Items".ljust(27) + " "*5 + "Amount".ljust(6) + " "*3 + "Item's price".rjust(12) + "\n" + "="*75

        option = getOpt(menuShowCust, flecha, [1,2,3,4])


        #CREAMOS UNA LISTA CON LOS DNI'S DE LOS CLIENTES QUE HAN COMPRADO
        list_compras = list(cliente_compra.keys())
        if option == 1:
            print(capPurch)
            #COMPROBAMOS QUE EL DNI DE LA PERSONA ESTA RELACIONADO CON ALGUNA COMPRA
            if DNI_glob in list_compras:
                seq = ""
                #MOSTRAMOS TODAS LAS COMPRAS REALIZADAS POR EL CLIENTE
                for Id_compra in cliente_compra[DNI_glob]:
                    total = 0
                    seq += Id_compra.ljust(11) + " "*4 + str(dict_compras[Id_compra]["fecha"]).ljust(8) + " "*4
                    for Id_articulo in dict_compras[Id_compra]["articulos"]:
                        total += dict_articulos[Id_articulo]["precio"] * dict_compras[Id_compra]["articulos"][Id_articulo]
                    seq += str(total).rjust(18) + "\n"
                print(seq)
            #SI SU DNI NO COINCIDE CON ALGUNA COMPRA SE MUESTRA UN ERROR
            else:
                print("The customer with NIF {} has not purchases".format(DNI_glob))
            input(press)

        elif option == 2:
            #COMPROBAMOS QUE EL DNI DE LA PERSONA ESTA RELACIONADO CON ALGUNA COMPRA
            if DNI_glob in list_compras:
                seq = ""
                #RECORREMOS TODAS LAS COMPRAS MOSTRANDO UNA TABLA DE INFORMACION INDIVIDUAL PARA CADA COMPRA
                for Id_compra in cliente_compra[DNI_glob]:
                    total = 0
                    #MOSTRAMOS LA CABECERA
                    print(capDetPurch)
                    #GUARDAMOS EN UNA CADENA LOS PRIMEROS DATOS
                    seq = Id_compra.ljust(5) + " "*5 + str(dict_compras[Id_compra]["fecha"]).ljust(8) + " "*4

                    #VARIABLE BOOLEANA PARA COMPROBAR SI ES LA PRIMERA ITERACIÓN
                    primero = True

                    #POR ESTÉTICA IMPRIMIREMOS LOS NOMBRES DE LOS ARTICULOS POR COLUMNAS ES POR ESO QUE EN LA ITERACION
                    #DE LOS ARTICULOS TENDREMOS QUE DISTINGUIR EL PRIMER ARTICULO QUE MOSTREMOS DEL RESTO

                    for id_item in dict_compras[Id_compra]["articulos"]:
                        if primero:
                            primero = False
                            seq += dict_articulos[id_item]["nombre"].ljust(27) + " "*5 + str(dict_compras[Id_compra]["articulos"][id_item]).ljust(6)
                            seq += " "*3 + str(dict_articulos[id_item]["precio"]).rjust(12) + "\n"
                            total += dict_articulos[id_item]["precio"] * dict_compras[Id_compra]["articulos"][id_item]
                        else:
                            seq += " "*22 + dict_articulos[id_item]["nombre"].ljust(27) + " " * 5 + str(
                                dict_compras[Id_compra]["articulos"][id_item]).ljust(6)
                            seq += " " * 3 + str(dict_articulos[id_item]["precio"]).rjust(12) + "\n"
                            total += dict_articulos[id_item]["precio"] * dict_compras[Id_compra]["articulos"][id_item]
                    seq += "-"*75 + "\n" + "Total".ljust(5) + str(total).rjust(70)
                    print(seq)

            # SI SU DNI NO COINCIDE CON ALGUNA COMPRA SE MUESTRA UN ERROR
            else:
                print("The customer with NIF {} has not purchases".format(DNI_glob))
            input(press)

        elif option == 3:
            #VOLVEMOS AL MAIN MENU
            menu321 = False
            menu00 = True
        elif option == 4:
            #VOLVEMOS AL MENU 32
            menu321 = False
            menu32 = True

