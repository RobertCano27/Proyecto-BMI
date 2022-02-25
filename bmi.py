def bmc(altura, peso):
        return peso / altura**2


peso = float(input('Escriba su peso (Kg): '))
altura = float(input('Escriba su estatura (m): '))

indice = peso / altura ** 2

print('Su BMC es: ' + str (round(indice,2)))
if indice >=0 and indice <= 16.9:
    print('Usted se encuentra en delgadez extrema')
elif indice >=17.0 and indice <= 18.4:
    print('Usted se encuentra en bajo peso')
elif indice >=18.5 and indice <= 24.9:
    print('SU peso es normal')
elif indice >=25.0 and indice <= 29.9:
    print('Usted se encuentra con sobre peso')
elif indice >=30.0 and indice <= 100:
    print('Usted se encuentra en estado de obecidad')
