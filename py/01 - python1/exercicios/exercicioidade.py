#  Copyright (c) 2020.  | All rights reserved
#  Mateus Borja // UX Designer • 3D Artist • Developer
#  www.mateusborja.life


ano_nascido = int(input('Qual ano voce nasceu: '))
ano_atual = 2020

idade = ano_atual - ano_nascido

if idade > 18:
    print("Você é um adulto e tem", idade, 'anos!')
elif idade < 4:
    print('Vocé é um bebê e tem apenas', idade, 'anos')
elif idade < 8:
    print('Vocé é uma criança tem apenas', idade, 'anos')
elif idade < 12:
    print('Vocé é um adolescente tem apenas', idade, 'anos')





