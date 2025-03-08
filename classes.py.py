# Definindo uma classe chamada "Carro"
class Carro:

    # Método inicializador (construtor) que define os atributos da classe
    def __init__(self, marca, modelo, ano):
        self.marca = marca
        self.modelo = modelo
        self.ano = ano 

    # Método para exibir informações sobre o carro
    def detalhes(self):
        return f"Carro: {self.marca} {self.modelo}, Ano: {self.ano}"

# Criando um objeto (instância) da classe Carro
meu_carro = Carro("Toyota", "Corolla", 2020)

# Chamando o método detalhes para exibir informações do carro
print(meu_carro.detalhes())
