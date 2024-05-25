#@classmethod
#@staticmethod

class MinhaClasse:
    valor = 10 #Atributo da classe

    def __init__(self, nome) -> None:
        self.nome = nome #Atributo da instância

    #Requer uma instância para ser chamado
    def metodo_instancia(self):
        return f"Método de instância chamado para {self.valor}"
    

    #Métodos da classe
    @classmethod #Utilizando o classmethod não precisa instanciar para ter acesso aos atributos e os métodos
    #nesse caso é utilizado a classe diretamente, lembrando sempre de adicionar o "cls"
    def metodo_classe(cls): #O método "cls" recebe a classe acessando todos os métodos e atributos, da mesma forma que o "self" recebe a instância
        return f"Método da classe chamado para valor={cls.valor}" #NÂO acessa aos atributos da instância
    

    @staticmethod #Diferente dos demais métodos pois não recebe nenhum argumento, não tem acesso aos atributos
    #da instância ou da classe, mas pode executar uma função específica, dobrar um valor, por exemplo
    #PRINCIPAL DIFERENÇA = classmethod recebe a referência da classe (cls) já o staticmethod não recebe e
    #o METODO DA INSTANCIA recebe a referencia da instância (self) tendo acesso aos atributos da instância e da classe.
    def metodo_estatico():
        return "Método estático"


obj = MinhaClasse(nome="Classe Exemplo")
print(obj.metodo_instancia())
print(MinhaClasse.valor)
print(MinhaClasse.metodo_classe())
print(MinhaClasse.metodo_estatico())

class Carro:
    def __init__(self, marca, modelo, ano) -> None:
        self.marca = marca
        self.modelo = modelo
        self.ano = ano

    @classmethod #Usado de maneira global, ou seja fora da classe ou através de parametros
    def criar_carro(cls, configuracao):
        marca, modelo, ano = configuracao.split(",")
        return cls(marca, modelo, ano)

configuracao1 = "Toyota,Corolla,2022"
carro1 = Carro.criar_carro(configuracao1)
print(f"Marca: {carro1.marca}\nModelo: {carro1.modelo}\nAno: {carro1.ano}")

class Matematica:

    @staticmethod
    def somar(a,b):
        return a+b

print(Matematica.somar(a=10, b=15))