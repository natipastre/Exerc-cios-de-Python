from decimal import Decimal, getcontext

# Configuração da precisão decimal
getcontext().prec = 4

# Função de conversão
def converter_moeda(valor, taxa):
    return valor * Decimal(taxa)

# Função principal
def main():
    print("Bem vindo à calculadora de Conversão de Moedas!")

    # Taxas de câmbio
    taxas = {
        "1": Decimal("0.19"),  # Dólar (1/5.25)
        "2": Decimal("0.18"),  # Euro (1/5.63)
        "3": Decimal("27.03"),  # Iene japonês (1/0.037)
        "4": Decimal("0.67"),  # Novo Shekel israelense (1/1.48)
        "5": Decimal("4.76"),  # Peso cubano (1/0.21)
    }

    valor_real = Decimal(input("Digite o valor em Reais (BRL): "))

    print("\nEscolha a moeda para a qual deseja converter:")
    print("1 - Dólar (USD)")
    print("2 - Euro (EUR)")
    print("3 - Iene japonês (JPY)")
    print("4 - Novo Shekel Israelense (ILS)")
    print("5 - Peso cubano (CUP)")

    escolha = input("Digite o número da opção desejada:")

    if escolha in taxas:
        valor_convertido = converter_moeda(valor_real, taxas[escolha])
        print(f"\nO Valor de R${valor_real:.2f} corresponde a {valor_convertido:.2f} na moeda escolhida.")
    else:
        print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    main()
