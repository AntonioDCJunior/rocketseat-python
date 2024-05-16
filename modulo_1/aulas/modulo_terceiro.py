#Pacotes ou bibliotecas criados por terceiros e não fazem parte dos pacotes padrão do PYTHON

print("\nImportação e uso de módulos de terceiros:")
import requests

url = "https://example.com"
response = requests.get(url)
print(f"Solicitação http para {url} retornou o status {response.status_code}")