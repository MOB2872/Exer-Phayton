#Tendo como dado de entrada a altura (h) de uma pessoa, construa um algoritmo que calcule seu peso ideal, utilizando as seguintes fórmulas
if __name__ == '__main__':
    altura = float(input("Digite a altura do homem (em metros): "))
    peso = round((72.7 * altura) - 58, 2)

    altura1 = float(input("Digite a altura da mulher (em metros): "))
    peso1 = round((62.1 * altura1) - 44.7, 2)

    print(f"O peso ideal do homem é: {peso} kg, e o peso ideal da mulher é: {peso1} kg")
