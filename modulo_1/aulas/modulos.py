#Arquivos que contem definições e instruções que podem ser utilizados em outros programas/arquivos

print("Exemplo de importação de módulo padrão:")
#importando o módulo completo de MATH: import math
#importando apenas SQRT (melhor prática, pois caso haja attualização no módulo completo, pode ocorrer erros)
from math import sqrt

raiz_quadrada = sqrt(25)
print(f"A raiz quadrada de 25 é: {raiz_quadrada}")

print("\n Exemplo de criação de utilização de um módulo personalizado")
#import meu_modulo
from meu_modulo import saudacao, dobro

mensagem = saudacao("Gabriel")
print(mensagem)
resultado_dobro = dobro(5)
print(f"O dobro de 5 é: {resultado_dobro}")