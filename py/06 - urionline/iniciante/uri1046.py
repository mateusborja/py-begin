#  Copyright (c) 2020.  | All rights reserved
#  Mateus Borja // UX Designer • 3D Artist • Developer
#  www.mateusborja.life

valores = input().split()
valores = list(map(int,valores))

h1, h2 = valores

if(h1 == h2):
	print('O JOGO DUROU %d HORA(S)' %24)
else:
	if(h2 < h1):
		print('O JOGO DUROU %d HORA(S)' %((24 - h1) + h2))
	else:
		print('O JOGO DUROU %d HORA(S)' %(h2 - h1))
