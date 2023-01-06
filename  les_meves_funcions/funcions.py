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







