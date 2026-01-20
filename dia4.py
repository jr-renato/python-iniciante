numero = int(input("Digite um número: "))

for i in range(1,11):
    print(numero, "x", i, "=", numero * i)

senha =""
while senha != "phyton":
    senha = input("Digite sua senha: ")
print("Acesso liberado")