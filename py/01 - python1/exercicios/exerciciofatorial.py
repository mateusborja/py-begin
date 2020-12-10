#  Copyright (c) 2020.  | All rights reserved
#  Mateus Borja // UX Designer • 3D Artist • Developer
#  www.mateusborja.life

#5 = 5 * 4 * 3 * 2 * 1 = 120 // calc fatorial

ct = 1
numero = int(input('Informe o numero: '))
fatorial = numero

while ((numero - ct) > 1):
    fatorial = fatorial * (numero - ct)
    ct += 1
print('Fatorial de', numero, 'e', fatorial)
print('Fatorial de {0} é: {1}'.format(numero,fatorial))


