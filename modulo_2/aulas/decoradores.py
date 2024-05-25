#Tipo especial de função que permite modificar ou estender o comportamento de outras funções
#Pode-se adicionar funcionalidades a funções ou métodos sem a necessidade de alterar o código original

from typing import Any


def meu_decorador(func):
    def wrapper():
        print("Antes da função se chamada")
        func()
        print("Depois da função se chamada")
    return wrapper

@meu_decorador
def minha_funcao():
    print("Minha função foi chamada")

minha_funcao()

#Usando decorador como classe
class MeuDecoradorDeClasse:
    def __init__(self, func) -> None:
        self.func = func 

    def __call__(self) -> Any:
        print("Antes da função ser chamada (decorador de classe)")
        self.func()
        print("Depois da função ser chamada (decorador de classe)")

@MeuDecoradorDeClasse
def segunda_funcao():
    print("Segunda função foi chamada")

segunda_funcao()