# Sportininko pasirodymą vertina trys teisėjai, skirdami T1, T2, T3 balų. 
# Reikia apskaičiuoti bendrąjį įvertinimą, kuris gaunamas atmetus vidurinį balą ir 
# imant kitų dviejų vidurkį.

def ivedimas():
    t1 = int(input('koks pirmo teisejo vertinimas? '))
    t2 = int(input('koks antro teisejo vertinimas? '))
    t3 = int(input('koks trecio teisejo vertinimas? '))
    return t1, t2, t3

def vidurkis(t1, t2, t3):
    vid = (t1 + t3) / 2
    return vid

t1, t2, t3 = ivedimas()
vid = round(vidurkis(t1, t2, t3))

print(f'{vid}')