from dades import *

#Ex 1
def getOpt(textOpts="",inputOptText="",rangeList=[],dictionary={},exceptions=[]):
    correct = False
    while not correct:
        print(textOpts)
        opc = input(inputOptText)
        try:
            if opc not in rangeList or opc not in exceptions:
                raise ValueError('Invalid option')
            else:








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