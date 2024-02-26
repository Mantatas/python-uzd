# Petriukas iš namų išvyko isvykoVal val. ir isvykoMin min.. Į mokyklą Petriukas atvyko atvykoVal val. ir atvykoMin
# min. Kiek valandų ir minučių Petriukas užtrūko kelyje?

isvykoVal = int(input('kokia valanda isvyko?' ))
isvykoMin = int(input('ir kuria minute?' ))
atvykoVal = int(input('kokia valanda atvyko? '))
atvykoMin = int(input('ir kuria minute? '))

trukmeMin = atvykoMin - isvykoMin
trukmeVal = atvykoVal - isvykoVal

if trukmeMin < 0:
    trukmeVal -=1
    trukmeMin +=60

if trukmeVal < 0:
    trukmeVal +=24

print(f'petro atvyko per {trukmeVal} valanda ir {trukmeMin} minute')

# += and -= Operators:
# += and -= are assignment operators.
# += is used for addition assignment, and it adds the right operand to the left operand.
# -= is used for subtraction assignment, and it subtracts the right operand from the left operand.