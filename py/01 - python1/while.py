#  Copyright (c) 2020.  | All rights reserved
#  Mateus Borja // UX Designer • 3D Artist • Developer
#  www.mateusborja.life

import time

contador = 1

while contador < 8:
    print('repetindo pela', contador, 'o. vez')
    contador += 1
    if contador == 6:
        break
    time.sleep(1)

print('terminou!')
