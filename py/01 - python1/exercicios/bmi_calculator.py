#  Copyright (c) 2020.  | All rights reserved
#  Mateus Borja // UX Designer • 3D Artist • Developer
#  www.mateusborja.life

# bmi calculator

name1 = "John"
height_m1 = 2
weight_kg1 = 90

name2 = "Mathews"
height_m2 = 1.8
weight_kg2 = 70

name3 = "Philip"
height_m3 = 2.5
weight_kg3 = 160


def bmi_calculator(name, height_m, weight_kg):
    bmi = weight_kg / (height_m ** 2)
    print("bmi: ")
    print("%1.2f" % (bmi))
    if bmi < 25:
        print(name + " not overweight")
    else:
        print(name + " is overweight")
    print()


bmi_calculator(name1, height_m1, weight_kg1)
bmi_calculator(name2, height_m2, weight_kg2)
bmi_calculator(name3, height_m3, weight_kg3)
