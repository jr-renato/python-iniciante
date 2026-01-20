nota = float(input("Digite sua nota (De 0 a 10): "))

while nota <0 or nota >10:
    print("Nota inválida, digite novamente")
    nota = float(input("Digite sua nota (De 0 a 10): "))

print("Nota registrada com sucesso")