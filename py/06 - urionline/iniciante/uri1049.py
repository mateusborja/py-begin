#  Copyright (c) 2020.  | All rights reserved
#  Mateus Borja // UX Designer • 3D Artist • Developer
#  www.mateusborja.life


palavra1 = input()
palavra2 = input()
palavra3 = input()

if palavra1 == "vertebrado":
    if palavra2 == "ave":
        if palavra3 == "carnivoro":
            print("aguia")
        else:
            print("pomba")
    else:
        if palavra3 == "onivoro":
            print("homem")
        else:
            print("vaca")
else:
    if palavra2 == "inseto":
        if palavra3 == "hematofago":
            print("pulga")
        else:
            print("lagarta")
    else:
        if palavra3 == "hematofago":
            print("sanguessuga")
        else:
            print("minhoca")
