#Exemplo de HERANÇA SIMPLES
class Animal:
    def __init__(self, nome) -> None:
        self.nome = nome

    def emitir_som(self):
        pass

class Mamifero(Animal):
    def amamentar(self):
        return(f"{self.nome} está amamentando")
    
class Ave(Animal):
    def voar(self):
        return(f"{self.nome} está voando")

#HERANÇA MULTIPLA
class Morcego(Mamifero, Ave):
    def emitir_som(self):
        return "Morcegos emitem sons ultrassônicos"
    
morcego = Morcego(nome="Batman")

#Acessando os métodos da classe base "Animal"
print("Nome do morcego:", morcego.nome)
print("Som do morcego:", morcego.emitir_som())


#Acessando os métodos das classes "Mamífero" e "Ave"
print("Morcego amamentando:", morcego.amamentar())
print("Morcego voando:", morcego.voar())


