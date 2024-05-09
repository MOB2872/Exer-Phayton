#Faça um Programa que peça a temperatura em graus Celsius, transforme e mostre em graus Farenheit.
if __name__ == '__main__':
    celsius = raw_input("Digite a temperatura em celsius: ")

    farenheit = ((float(celsius) + 32) / 5) * 9

    print("%.2f graus farenheit" % farenheit)
