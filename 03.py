# Programuotojų konkurse reikia išspręsti penkias užduotis. Konkurso taisyklės yra sudėtingos 
# ir nebūtinai sąžiningos: Pirmas uždavinys vertas 10 taškų, antras uždavinys – 20 taškų 
# trečias uždavinys – 30 taškų, ketvirtas uždavinys – 40 taškų, penktas uždavinys – 50 taškų. 
# Jei dalyvis išsprendžia visus uždavinius, papildomai gauna 50 taškų. Tai iš viso sudarys 
# 200 taškų. Jei dalyvis išsprendžia pirmą ir paskutinį uždavinius, gauna papildomai 20 taškų. 
# Tai iš viso sudarys 80 taškų. Jei dalyvis išsprendžia trečią ir ketvirtą uždavinius, 
# bet neišsprendžia pirmo arba antro, tuomet gauna tik 50 taškų. Jei dalyvis neišsprendžia 
# pirmo, antro ir trečio uždavinio, tuomet už likusius du uždavinius gauna 50 procentų mažiau 
# taškų. Visais kitais atvejais dalyvis gauna 0 taškų. Ar atlikta užduotis, ar ne rodo 
# skaičiukai: 1–reiškia, kad uždavinys atliktas, 0 –uždavinys neatliktasir vertinamas 0 taškų.
# Programai pateikiami dviejų programuotojų duomenys, kuriuos uždavinius išsprendė, kurių 
# nesugebėjo atlikti.Reikia nustatyti, kuris programuotojas laimėjo, pirmas ar antras. 
# Jei abu programuotojai surinko vienodai taškų, tuomet skelbiamos lygiosios.

vQ1 = int(input('ar pirmas dalyvis issprende pirma? (1 - taip, 0 - ne) '))
aQ1 = int(input('ar antras dalyvis issprende pirma? (1 - taip, 0 - ne) '))
vQ2 = int(input('ar pirmas dalyvis issprende antra? (1 - taip, 0 - ne) '))
aQ2 = int(input('ar antras dalyvis issprende antra? (1 - taip, 0 - ne) '))
vQ3 = int(input('ar pirmas dalyvis issprende trecia? (1 - taip, 0 - ne) '))
aQ3 = int(input('ar antras dalyvis issprende trecia? (1 - taip, 0 - ne) '))
vQ4 = int(input('ar pirmas dalyvis issprende ketvirta? (1 - taip, 0 - ne) '))
aQ4 = int(input('ar antras dalyvis issprende ketvirta? (1 - taip, 0 - ne) '))
vQ5 = int(input('ar pirmas dalyvis issprende penkta? (1 - taip, 0 - ne) '))
aQ5 = int(input('ar antras dalyvis issprende penkta? (1 - taip, 0 - ne) '))

if vQ1 and vQ2 and vQ3 and vQ4 and vQ5 == 1:
    vTsk = 200
elif vQ1 and vQ5 == 1:
    vTsk = 80
elif (vQ3 and vQ4 == 1) and (vQ1 or vQ2 == 0):
    vTsk = 50
elif vQ1 and vQ2 and vQ3 == 0:
    vTsk = vTsk / 2
else:
    vTsk = 0

if aQ1 and aQ2 and aQ3 and aQ4 and aQ5 == 1:
    aTsk = 200
elif aQ1 and aQ5 == 1:
    aTsk = 80
elif (aQ3 and aQ4 == 1) and (aQ1 or aQ2 == 0):
    aTsk = 50
elif aQ1 and aQ2 and aQ3 == 0:
    aTsk = aTsk / 2
else:
    aTsk = 0

def kurisDaugiau(vTsk, aTsk):
    if vTsk > aTsk:
        return f'pirmas laimejo surinkes {vTsk}'
    if aTsk > vTsk:
        return f'antras laimejo surinkes {aTsk}'
    else:
        return 'lygiosios'
    
rez = kurisDaugiau(vTsk, aTsk)
print (f'pirmas surinko {vTsk}, antras surinko {aTsk}. {rez}')