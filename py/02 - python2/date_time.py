#  Copyright (c) 2020.  | All rights reserved
#  Mateus Borja // UX Designer • 3D Artist • Developer
#  www.mateusborja.life

from datetime import date
import datetime

print(datetime.date.today().day)

if datetime.date.today().day == 9:
    print("hoje e o seu dia!", date.today().day)
else:
    print("hoje nao e seu dia!")

print(date.isoformat(date.today()))

