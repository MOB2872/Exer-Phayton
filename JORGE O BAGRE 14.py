LIMITE = 50
MULTA = 4.0

excesso = 0.0
peso = input("Digite o peso dos peixes: ")

if float(peso) > LIMITE:
    excesso = (float(peso) - LIMITE) * MULTA
    print("O valor da multa é de R$ %.2f" % excesso)
else:
    print("Excesso: %.2f" % excesso)
