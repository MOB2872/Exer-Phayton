#Faça um Programa que peça a temperatura em graus Farenheit, transforme e mostre a temperatura em graus Celsius.
if __name__ == '__main__':
    farenheit = raw_input("Digite a temperatura em Farenheit: ")

    celsius = (5 * (float(farenheit) - 32) / 9)

    print("%.2f graus celsius" % celsius)
