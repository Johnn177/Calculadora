def suma():
    x = input('Ingrese el primer numero: ')
    y = input('Ingrese el segundo numero: ')
    return int(x)+int(y)
def resta():
    x = input('Ingrese el primer numero: ')
    y = input('Ingrese el segundo numero: ')
    return int(x) - int(y)
def mul():
    x = input('Ingrese el primer numero: ')
    y = input('Ingrese el segundo numero: ')
    return int(x) * int(y)
def div():
    x = input('Ingrese el primer numero: ')
    y = input('Ingrese el segundo numero: ')
    return int(x)/int(y)
sw=True

menu = '''
========Calculadora========
1.Sumar
2.Restar
3.Multiplicar
4.Dividir
5.Salir
'''
while sw:
    swa = True
    while swa:
        print(menu)
        a = int(input('Elija una opción: '))
        if a == 1:
            print(f'La suma es: {suma()}')
            swa=False
        elif a==2:
            print(f'La resta es: {resta()}')
            swa = False
        elif a==3:
            print(f'La multiplicación es: {mul()}')
            swa = False
        elif a==4:
            print(f'La division es: {div()}')
            swa = False
        elif a==5:
            swa = False
            sw=False
        else:
            print('Opcion no valida')
