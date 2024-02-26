# Tarakonas yra vienas greičiausių gyvūnų. Jo greitis yra greitisPerValanda kilometrų per valandą. Apskaičiuokite, 
# kiek centimetrų keliasCmPerS tarakonas nubėga per sekundę. 1 km/h = 27.77778 cm/s

greitPerH = float(input('koks tarakono greitis (km/h)? '))

kelCmPerS = greitPerH * 27.77778

print(f'tarakonas nubegs {round(kelCmPerS,)} cm')