#  Copyright (c) 2020.  | All rights reserved
#  Mateus Borja // UX Designer • 3D Artist • Developer
#  www.mateusborja.life

salario = float(input())
imposto = 0.0

if salario <= 2000.0:
    imposto = 0
elif salario > 2000.0 and salario <= 3000.0:
    imposto = (salario - 2000.0) * 0.08
elif salario > 3000.0 and salario <= 4500:
    imposto = (salario - 3000.0) * 0.18 + (1000 * 0.08)
elif salario > 4500.0:
    imposto = ((salario - 4500.0) * 0.28) + (1500.0 * 0.18) + (1000.0 * 0.08)

if (imposto == 0):
    print("Isento")
else:
    print("R$ %.2f" % imposto)
