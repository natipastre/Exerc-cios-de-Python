while True:
    try:
        numero = int(input("Digite um número: "))
        print(f"O dobro do número é: {numero * 2}")
        break  # Sai do loop se a entrada for válida
    except ValueError:
        print("Erro: Você deve digitar um número válido.")
