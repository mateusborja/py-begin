#  Copyright (c) 2020.  | All rights reserved
#  Mateus Borja // UX Designer • 3D Artist • Developer
#  www.mateusborja.life


a = 1
b = 3

for i in range(b):
    print('frase')

for i in range(3):
    a = a + 1
    print('{:.1f}'.format(i), a)

palavra = 'mateus borja'
for i in palavra:
    print(i)

z = []
for i in range(2):
    z.append(palavra)
palavra = ''.join(z)
print(z)

y = []
for i in range(5):
   y.append('X')
y = ' '.join(y)
print(y)

num = []
for i in range(5):
    num.append('a ')
num = ''.join(num)
print(num)



