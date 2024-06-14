# Jogo de combate, com dois jogadora (heroi e inimigo)
# Haverá tomadas de decisões relacionado ao ataque se será um ataque normal ou especial

# Inicialmente será usaod os conhecimentos sobre CLASSE

#Personagem: Classe mãe
#Heroi: controlado pelo usuário
#Inimigo: adversário

#Os personagens tem nome, vida e nível
#Vida: pra fazer o controle do dano recebido
#Nível: é o que vai ocasionar o dano, por exemplo, um hério nivel 15 terá uma intensidade maior que um de nível 2
#Será aplicado o conceito de ENCAPSULAMENTO, tornando os atributos privados 
class Personagem:
    def __init__(self, nome, vida, nivel) -> None:
        self.__nome = nome
        self.__vida = vida
        self.__nivel = nivel

    #Já que são privados, será necessário criar os GETRs, para recuperar os valores
    def get_nome(self):
        return self.__nome
    
    def get_vida(self):
        return self.__vida
    
    def get_nivel(self):
        return self.__nivel

    def exibir_detalhes(self):
        return f"Nome: {self.get_nome()}\nVida: {self.get_vida()}\nNível: {self.get_nivel()}"
    
    def receber_ataque(self, dano):
        self.__vida -= dano
        if self.__vida < 0:
            self.__vida = 0
    
    def atacar(self, alvo): #nesse caso não é necessário usar o "get" pois estar na mesma classe, mas pode usar se quiser
        dano = self.__nivel * 2
        alvo.receber_ataque(dano)
        print(f"{self.get_nome()} atacou {alvo.get_nome()} e causou {dano} de dano!")

    

#Usado HERANÇA ao utilizar ATRIBUTOS e MÉTODOS de PERSONAGEM
#Usado ENCAPSULAMENTO ao proteger corretamente os atributos de cada classe usando o __, por isso foi usado o GET
#Houve uso de POLIMORFISMO, ao usar a classe mãe e reimplimentou o "exibir_detalhes"

class Heroi(Personagem): #Tem algo a mais que o Personagem "habilidade"
    def __init__(self, nome, vida, nivel, habilidade) -> None:
        super().__init__(nome, vida, nivel)
        self.__habilidade = habilidade

    def get_habilidade(self):
        return self.__habilidade
    
    def exibir_detalhes(self):
        return f"{super().exibir_detalhes()}\nHabilidade: {self.get_habilidade()}\n"   


class Inimigo(Personagem):
    def __init__(self, nome, vida, nivel, tipo) -> None:
        super().__init__(nome, vida, nivel)
        self.__tipo = tipo

    def get_tipo(self):
        return self.__tipo
    
    def exibir_detalhes(self):
        return f"{super().exibir_detalhes()}\nTipo: {self.get_tipo()}"


class Jogo:
    """ Classe Orquestradora do jogo """

    def __init__(self) -> None:
        self.heroi = Heroi(nome="Heroi", vida=100, nivel=5, habilidade="Super Força")
        self.inimigo = Inimigo(nome="Inimigo", vida=10, nivel=5, tipo="Voador")


    def iniciar_batalha(self):
        """ Fazer a gestão da batalha em turnos """

        print("Iniciando batalha!")
        #Haverá uma condição em que o jogo vai acontecer até alguém perder ou os dois perderem
        #and = verd e falso o jogo para
        #or = verd e falso o jogo iria continuar
        while self.heroi.get_vida() > 0 and self.inimigo.get_vida() > 0:
            print("\nDetalhes dos personagens:")
            print(self.heroi.exibir_detalhes())
            print(self.inimigo.exibir_detalhes())

            input("\nPressione ENTER para atacar...")
            escolha = input("\nEscolha (1 - Ataque Normal, 2 - Ataque Especial): ")

            if escolha == '1':
                self.heroi.atacar(self.inimigo)
            else:
                print("\nEscolha inválida. Escolha novamente!")

        #if self.heroi.get_vida() > 0 or self.inimigo.get_vida > 0:
        #    print("Parabéns você venceu a batalha!")
        #else:
        #    print("Ambos perderam")

        if self.heroi.get_vida() > 0:
            print("Parabéns você venceu a batalha!")
        else:
            print("Voceê foi derrotado")

#Criar instância do jogo e iniciar batalha

jogo = Jogo()
jogo.iniciar_batalha()


