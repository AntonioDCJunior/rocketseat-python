#abstração, encapsulamento, herança e polimorfismo = 
#são consideradas estratégias de uso e manipulação das estruturas (classe)

#Herança
print("\nExemplo de HERANÇA")
class Animal:
    def __init__(self, nome) -> None:
        self.nome = nome

    def andar(self):
        print(f"O animal {self.nome} andou")

    def emitir_som():
        #deixar passar caso deixe vazio. Esse método não faz nada
        pass

#O cachorro HERDOU tudo da classe mãe ANIMAL
#Está sendo usado também o POLIMORFISMO, ao utilizar o método emitir_som, porque nesse exmplo, o método está sendo 
#utilizado de diferentes formas, e a chamada do objeto é a mesma, a única coisa que muda é a forma de implementação
class Cachorro(Animal):
    def emitir_som(self):
        return "Au, au"    
    
class Gato(Animal):
    def emitir_som(self):
        return "Miau, miau"
    
dog = Cachorro(nome="Rex")
cat = Gato(nome="Felix")

print("\nExemplo de POLIMORFISMO")
animais = [dog, cat]

for animal in animais:
    print(f"{animal.nome} faz: {animal.emitir_som()}")

print("\nExemplo de ENCAPSULAMENTO")
class ContaBancaria:
    def __init__(self, saldo) -> None:
        self.__saldo = saldo #atributo privado, ou seja, outra classe não terá acesso, apenas os métodos que estão dentro da classe

    def depositar(self, valor):
        #se o valor é maior que zero, o saldo será aumentado no valor que foi depositado
        if valor > 0:
            self.__saldo += valor
    
    def sacar(self, valor):
        #se o valor do saque é maior que zero e é menor do que ele tem
        if valor > 0 and valor <= self.__saldo:
            #será subtraído o saldo da conta
            self.__saldo -= valor
    
    def consultar_saldo(self):
        return self.__saldo
    
conta = ContaBancaria(saldo=1000)
print(f"Saldo da conta bancária: {conta.consultar_saldo()}")

conta.depositar(valor=500)
print(f"Saldo da conta bancária, após depósito: {conta.consultar_saldo()}")

conta.depositar(valor=-500) #não foi realizada alteração de valor
print(f"Saldo da conta bancária: {conta.consultar_saldo()}")

conta.sacar(valor=2000) #não será alterado devido ao IF
print(f"Saldo da conta bancária, após saque: {conta.consultar_saldo()}")

print("\nExemplo de ABSTRAÇÃO")
from abc import ABC, abstractmethod

class Veiculo(ABC): #uma classe abstrata não possui implementação, ela é só um molde

    #usa-se decorador
    #quando criar uma classe derivada, a classe será obrigada a implementar os métodos da mesma, caso contrário
    #não será possível criá-la. Nesse caso os métodos: ligar e desligar
    #Dierente da HERANÇA, que 
    @abstractmethod
    def ligar(self):
        pass

    @abstractmethod
    def desligar(self):
        pass

class Carro(Veiculo):
    def __init__(self) -> None:
        pass

    def ligar(self):
        return "Carro ligado usando a chave"
    
    def desligar(self):
        return "Carro desligado usando a chave"

carro_amarelo = Carro()
print(carro_amarelo.ligar())
print(carro_amarelo.desligar())