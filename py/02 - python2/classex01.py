#  Copyright (c) 2020.  | All rights reserved
#  Mateus Borja // UX Designer • 3D Artist • Developer
#  www.mateusborja.life

class DidaticaT:  # didatica_tech
    def incrementa(self, v, i):  # self utilizada ao definir funcao dentro de classe
        valor = v
        incremento = i
        resultado = valor + incremento
        return resultado


a = DidaticaT()  # instancia da classe atribuido a variavel (objt)
b = a.incrementa(4, 1)  # chamando a instancia e a funcao

c = DidaticaT().incrementa(1, 4)  # chamando a classe e o metodo

print(a)  # imprimi local de memoria do objeto a que instanciou a classe
print(b)
print(c)


class DidaticaP:
    def incrementa(self, v, i):
        self.valor = v
        self.incremento = i
        self.resultado = self.valor + self.incremento
        return self.resultado


m = DidaticaP()
n = m.incrementa(10, 20)
m.valor

print(m.valor)
print(m.incremento)
print("soma:", n)


class DidaticaQ:
    def __init__(self, v: int, i: int):
        self.valor = v
        self.incremento = i
    def incrementa(self):
        self.valor = self.valor + self.incremento


o = DidaticaQ(10, 1)
print("soma e:",o.incrementa())
