from datetime import datetime

def calcular_idade(data_nascimento):
    # Obter a data atual
    data_atual = datetime.now()

    # Calcular a idade
    idade = data_atual.year - data_nascimento.year 

    # Verificar se a pessoa já fez aniversário este ano
    if (data_atual.month, data_atual.day) < (data_nascimento.month, data_nascimento.day):
        idade -= 1  # Subtrair 1 se ainda não fez aniversário

    return idade

def main():
    data_str = input("Digite sua data de nascimento (no formato DD/MM/AAAA): ")

    # Converter a string para uma data usando o formato especificado
    data_nascimento = datetime.strptime(data_str, "%d/%m/%Y")

    # Calcular e exibir a idade
    idade = calcular_idade(data_nascimento)
    print(f"Você tem {idade} anos.")

if __name__ == "__main__":
    main()
