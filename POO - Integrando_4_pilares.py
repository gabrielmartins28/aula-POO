#integrando os 4 piulares da POO
class Funcionario:
    def __init__(self, nome, salario):
        self.nome = nome
        self.__salario = salario
    def mostrar_dados(self):
        print(f"Funcionário: {self.nome}")

    def calcular_bonus(self):
        return self.__salario * 0.10 + self.__salario

class Gerente(Funcionario):
    def calcular_bonus(self):
        return 5000

class Desenvolvedor(Funcionario):
    def calcular_bonus(self):
        return 2000

gerente = Gerente("Carlos", 10000)
dev = Desenvolvedor("Ana", 8000)

gerente.calcular_bonus()
dev.calcular_bonus()
"""
CONCEITO----------------------
CLASSE---------------------- FUNC, GER, DEV
OBJETO---------------------- GERENTE1, DEV1
METODO---------------------- MOSTRAR_DADOS()
ATRIBUTO----------------------NOME, __SALARIO
ENCAPSULAMENTO---------------------- __SALARIO
HERANÇA---------------------- GERENTE(FUNCIONARIO)
POLIFOMISMO---------------------- CALCULAR_BONUS() --DIFERENTE EM CADA CLASSE
"""