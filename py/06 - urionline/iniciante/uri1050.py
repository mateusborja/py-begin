#  Copyright (c) 2020.  | All rights reserved
#  Mateus Borja // UX Designer • 3D Artist • Developer
#  www.mateusborja.life


ddd = input()

list = {"61": "Brasilia", "71": "Salvador", "11": "Sao Paulo", "21": "Rio de Janeiro", "32": "Juiz de Fora",
        "19": "Campinas", "27": "Vitoria", "31": "Belo Horizonte"}

try:
    print(list[ddd])
except:
    print("DDD nao cadastrado")
