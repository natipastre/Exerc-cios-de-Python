# Função para converter Celsius para Fahrenheit
def celsius_para_fahrenheit(celsius):
    return (celsius * 9/5) + 32

# Função para converter Fahrenheit para Celsius
def fahrenheit_para_celsius(fahrenheit):
    return (fahrenheit - 32) * 5/9

# Menu para usuário
def menu():
    while True:  # Cria um loop para repetir o menu até o usuário escolher sair
        print("Escolha uma das opções:")
        print("1 - Converter Celsius para Fahrenheit")
        print("2 - Converter Fahrenheit para Celsius")
        print("3 - Sair")

        # Recebe a opção do usuário
        opcao = input("Digite a opção: ")

        if opcao == "3":
            print("Saindo do programa.")
            break  # Sai do loop e finaliza o programa

        if opcao in ["1", "2"]:
            temperatura = float(input("Digite a temperatura: "))

            if opcao == "1":
                resultado = celsius_para_fahrenheit(temperatura)
                print(f"{temperatura} ºC é igual a {resultado} ºF")
            elif opcao == "2":
                resultado = fahrenheit_para_celsius(temperatura)
                print(f"{temperatura} ºF é igual a {resultado} ºC")
        else:
            print("Opção inválida. Tente novamente.")

# Chama a função menu para iniciar o programa
menu()
