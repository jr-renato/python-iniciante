compras = []

compras.append("Arroz")
compras.append("Feijão")
compras.append("Leite")

for item in compras:
    print(item)

nomes = []
for i in range(3):
    nome = input("Digite seu nome: ")
    nomes.append(nome)
print("\nNomes digitados: ")
for nome in nomes:
    print(nome)

numeros = [10, 3, 7, 1]

for n in numeros:
    if n >= 5:
        print(n, "É igual ou maior que 5")