# Keliamaisiais vadinami metai, kurie nėra šimtmečio metai ir be liekanos dalijasi iš 4, arba tie, kurie yra 
# šimtmečio metai ir be liekanos dalijasi iš 400. Parenkite programą, kuri, įvedus žmogaus gimimo metus m, 
# nustatytų, ar žmogus gimė keliamaisiais ar ne keliamaisiais metais

def arKel(metai):
    if (metai % 4 == 0 and metai % 100 != 0) or (metai % 400 == 0):
        return True
    else:
        return False
    
metai = int(input("gimimo metai? "))

if arKel(metai):
    print(f'{metai} yra keliamieji metai')
else:
    print(f'{metai} nera keliamieji metai')