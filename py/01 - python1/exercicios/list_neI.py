#  Copyright (c) 2020.  | All rights reserved
#  Mateus Borja // UX Designer • 3D Artist • Developer
#  www.mateusborja.life

print("Digite o nome: ")
func = input()

list = {"Mateus": "Developer Java", "Felipe": "Developer C++", "Joao": "Developer C#"}

try:
    print(list[func])
except:
    print("Não esta na lista")


