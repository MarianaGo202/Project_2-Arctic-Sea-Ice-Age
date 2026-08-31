import os

pasta = "dados_brutos"

print("Pasta dos dados:")
print(os.path.abspath(pasta))

print("\nArquivos encontrados:")

for arquivo in os.listdir(pasta):
    print(arquivo)
    