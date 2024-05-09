if __name__ == '__main__':
    valor_hora = float(input("Digite o valor ganho por hora de trabalho: "))

    horas_trabalhadas = float(input("Digite o valor de horas trabalhadas neste mês: "))

    pagamento = valor_hora * horas_trabalhadas

    print("Você trabalhou por",horas_trabalhadas,"horas.")

    print("O valor da hora trabalhada é de R$",valor_hora)

    print("O pagamento que deve ser recebido é de: R$",pagamento)

