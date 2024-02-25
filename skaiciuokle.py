# suprogramuoti skaiciuotuva. veiksmai +, -, /, *, ^ (kelimas laipsniu)
# q - saknies traukimas butinai naudoti math.sqrt(x)
# rezultato isvedimas
# rezultatas = 15 BLOGAI 
# 5 + 10 = 15
# arba 5 * 4 = 20
# is skaiciaus 16 istraukus sakni gausim 4
# 5 ^ 3 = 125
# povandeniniai akmenys dalyba is nulio, saknies traukimas is neigiamo
# jei pasirinkome operacija q antro sk neivedame. NEKARTOTI KODO

#*** pasirinkus bloga operacija tarkin @ pranesama blogai pasirinkta operacija ir prasoma kartoti operacijos pasirinkima

import math

def ivedimas():
    x = int(input('koks pirmas skaicius? '))
    opr = input('kokia operacija? ')

    if opr == 'q':
        return x, None, opr
    
    y = int(input('koks antras skaicius? '))
    return x, y, opr

def operacija(x, y, opr):
    if opr == '+':
        rez = x + y
        return f'{x} {opr} {y} = {rez}'
    elif opr == "-":
        rez = x - y
        return f'{x} {opr} {y} = {rez}'
    elif opr == "*":
        rez = x * y
        return f'{x} {opr} {y} = {rez}'
    elif opr == "/":
        if y == 0:
            return 'dalyba is 0 negalima!'
        rez = round(x / y)
        return f'{x} {opr} {y} = {rez}'
    elif opr == "q":
        if x <= 0:
            return 'saknies traukimas is neigiamo sk neimanomas'
        rez = round(math.sqrt(x))
        return f'saknies traukimas is {x} = {rez}'
    elif opr == "^":
        rez = x**y
        return f'{x} pakelus {y} gausime {rez}'
    else:
        return 'blogai pasirinkta operacija'
    
x, y, opr = ivedimas()
rezul = operacija(x, y, opr)
print(rezul)