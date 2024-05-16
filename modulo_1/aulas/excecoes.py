#Eventos que ocorrem durante a execução do código, vindo a interromper a execução do programa.
#Quando não tratada pode gerar bug
#Usa-se o TRY, em python chama-se try execpt

print("Exemplo de captura de exceções")
try:
    numero = int(input("Digite um número inteiro: "))
    resultado = 10 / numero
    print(f"Resultado: {resultado}")
except Exception as e:
    print(f"Erro: {e}")