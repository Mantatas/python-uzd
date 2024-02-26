# Vienas garsus Lietuvos pramogų pasaulio atstovas per kito garsaus pramogų atstovo vestuves klaidingai informavo 
# policiją apie užminuotą pokylio vietą. Teismas paskyrė sumokėti baudosDydis eurų baudą. Kaltininkas baudą nutarė 
# sumokėti 1 cento monetomis. Apie 1 cento monetą yra žinoma, kad jos skersmuo yra 16,25 mm, storis – 1,67 mm, o 
# svoris – 2,3 g.
# 1. Kiek kilogramų monetų buvo nuvežta į banką (atsakymą suapvalinkite iki 3 skaičių po kablelio)?
# 2. Kokio aukščio bokštą (metrais) galima pastatyti iš monetų (atsakymą suapvalinkite iki 2 skaičių po kablelio)?
# 3. Kokio dydžio kvadratą, užpildytą monetomis, galima sudėlioti iš šių monetų (iš kiek monetų sudaryta 
# kvadrato kraštinė?), kiek monetų sunaudota visam kvadratui, kiek monetų liko nepanaudota?
# 4. Kokį plotą (m2) užima tas kvadratas (kvadratas iš 3 dalies) (atsakymą suapvalinkite iki 4 skaičių po kablelio)?

import math

MONETOS_MASE = 2.3 #g
MONETOS_SKERSMUO = 16.25 #mm
MONETOS_STORIS = 1.67 #mm

baudosDydis = int(input('koks baudos dydis? '))
baudosDydis = baudosDydis * 100 # monetu sk. kito kintamo nereikia.
centSkers = MONETOS_SKERSMUO / 1000
centStor = MONETOS_STORIS / 1000
centSvor = MONETOS_MASE / 1000

centSv = round((baudosDydis * centSvor), 3)
bokst = round((baudosDydis * centStor), 2)
kvKrastine = math.trunc(math.sqrt(baudosDydis))
kiekSunaudota = kvKrastine**2
atlMon = baudosDydis - kiekSunaudota
krMetrais = (kvKrastine * MONETOS_SKERSMUO)/1000
uzPlotas = round((krMetrais**2), 4)

print(f'i banka buvo nuvezta {centSv} kg monetu')
print(f'is ju galima padaryti {bokst} metru boksta')
print(f'kvadrato skersmuo butu sudarytas is {kvKrastine} monetu, sunaudota {kiekSunaudota} ir atliko {atlMon} monetu')
print(f'kvadrato plotas butu {uzPlotas} kv. metrai')
