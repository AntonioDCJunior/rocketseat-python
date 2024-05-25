#Uma linguagem de programação orientada a objetos adota conceitos de programação orientada a objetos,
#criando softwares modulares, reutilizável sendo mais fácil de se entender e manter.
#POO é um paradgma de programaçãol que se baseia na organização de programas em torno de Objetos, os quais são instâncias de classe
#Quando se fala em POO, deve-se lembrar de CLASSES e OBJETOS
#Pilares: encapsulamento, herança, polimorfismo e abstração

#Uma CLASSE é um modelo, um plano que define a estrutura e o comportamento dos OBJETOS, composto por:
#atributos e métodos, que são ações dos OBJETOS
class Pessoa:
    # "init" dentro de uma classe é um método, fora é uma função
    #o SELF é uma referência a própria classe, para que possa utilizar os métodos e atributos da classe
    # -> None: não é obrigatório, serve apenas para dizer que o método não tem retorno
    def __init__(self, nome, idade) -> None:
        self.nome = nome
        self.idade = idade

    def saudacao(self):
        return f"Olá, meu nome é {self.nome} eu tenho {self.idade} anos"

#Objetos: é uma instância da CLASSE, ele é criado a partir da CLASSE, podendo representar entidades do mundo real
pessoa1 = Pessoa("Alice", 30)
mensagem = pessoa1.saudacao()
print(mensagem)

#outra forma de usar o paradgma de POO
pessoa2 = Pessoa(nome="Rodrigo", idade=32)
mensagem = pessoa2.saudacao()
print(mensagem)