#Bloco de código reutilizável

def saudacao(nome):
    print(f"Olá, {nome}!")

print("\n Chamando a função saudação:")
saudacao("Alice")
saudacao("Bob")

#função com retorno
def quadrado(numero):
    resultado = numero ** 2
    return resultado

print("\n Chamando função quadrado:")
resultado_quadrado = quadrado(6)
print("Resultado: ", resultado_quadrado)

#Função com multiplos parâmatros
def soma(numero1, numero2):
    resultado = numero1 + numero2
    return resultado

print("\nChamando a função soma:")
numero1 = 30
numero2 = 10
resultado_soma = soma (numero1, numero2)
print("O resultado da soma %s com %s é: %s " %(numero1, numero2, resultado_soma))