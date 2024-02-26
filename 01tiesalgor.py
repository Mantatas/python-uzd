# Vos baigęs 12 klasių Petriukas nutarė užsiimti statybos verslu. Pirmą užsakymą jis gavo iš savo močiutės. 
# Plytelėmis, kurių matmenys plytelesIlgis ir plytelesPlotis (duomenys pateikiami centimetrais! Sveikieji skaičiai tarkim 
# 30 40.) reikia išklijuoti garažą, kurio matmenys garazoIlgis ir garazoPlotis (duomenys pateikti metrais! Gali būti ir 
# realieji skaičiai tarkim 6.2 ir 7.8). Matematika jam sekėsi prastai, tačiau jis mokėjo truputi programuoti, bet nemokėjo 
# sąlygos ir ciklo sakinių. Tad nutarė parašyti programą, kuri jam padėtų apskaičiuoti, kiek plytelių jam reikės nusipirkti. 
# Berašydamas programą, sužinojo, kad statybinių prekių parduotuvė „Senukai“ parduoda plyteles tik sveikomis 
# pakuotėmis (neardo pakuočių), kuriose yra plyteliuSkaiciusPakuoteje plytelių ir kaina yra nurodyta 1 m2
# (vienoMKaina). Bežiūrėdamas https://www.youtube.com/ metodinę medžiagą „Kaip klijuoti plyteles“, pastebėjo, 
# kad tarp plytelių yra paliekamas 2 mm tarpelis. Kad būtų lengviau programuoti, jis nutarė pakartotinai nenaudoti 
# nupjautos plytelės likučio. 
# Parašykite programą, kurioje suvedus „paryškintus“ duomenis programa pateiktų rezultatą kiek reikės 
# plytelių iš ilgio, kiek jų reikės iš pločio , kiek plytelių reikės iš viso, kiek pakuočių Petriukas privalo nusipirkti ir kiek 
# kainuos visos plytelės. 
# Kadangi Petriukas sąžiningas žmogus, jis nutarė dar pateikti ir ataskaitą kiek plytelių liko nepanaudotų
# ir kokia jų kaina.

import math

plytIlgis = int(input('koks plyteles ilgis centimetrais? '))
plytPlotis = int(input('koks plyteles plotis centimetrais? '))
garIlgis = float(input('koks garazo ilgis metrais? '))
garPlotis = float(input('koks garazo plotis metrais? '))
plytKiekis = int(input('kiek plyteliu pakuoteje? '))
m2Kaina = float(input('kokia pakuotes kaina evrais? '))

plytIlgis = plytIlgis / 100
plytPlotis = plytPlotis / 100

plytPerKv = math.floor(10000 / (plytIlgis + 0.2) * (plytPlotis + 0.2))
plytPerIlgi = garIlgis / plytIlgis
plytPerPloti = garPlotis / plytPlotis
visoPlytu = plytPerIlgi * plytPerPloti
pakKiekis = (visoPlytu / plytKiekis)
visKaina = visoPlytu / plytPerKv * m2Kaina
likPlyt = plytPerKv * plytKiekis - visoPlytu
likKaina = likPlyt // plytPerKv * m2Kaina

print(f'reikes {plytPerIlgi} plytu per ilgi, {plytPerPloti} plytu per ploti ir {visoPlytu}'
      f' is viso. reikes nupirkti {pakKiekis} pakuociu ir jos kainuos {visKaina}.'
      f' atliks {likPlyt} plyteliu ir ju kaina {likKaina}')