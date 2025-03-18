#O programa deverá iniciar com a criação de uma classe chamada “Carro”, contendo um método “tipo_carro” que retorna a mensagem “Este é um carro”.
Será criada uma subclasse chamada “CarroEsportivo”, que herda de “Carro”, e o método “tipo_carro” será sobrescrito para retornar a mensagem “Este é um carro esportivo”.
Em seguida, será criada a subclasse “CarroFamilia”, também herdando de “Carro”, e o método “tipo_carro” será para retornar a mensagem “Este é um carro de família”.
Será criada a subclasse “CarroSUV”, que herda de “Carro”, e o método “tipo_carro” será sobrescrito para retornar a mensagem “Este é um carro SUV”.
O programa deverá instanciar as variáveis carro, carro_esportivo, carro_familia e carro_suv com os respecitivos objetos das classes criadas.
Utilizar o comando print para exibir no console a mensagem de cada objeto, chamando o método tipo_carro de cada instância.
testar o programa para garantir que a saída está correta e que cada tipo de carro é exibido corretamente no console


# Classe base Carro
class Carro:
    def tipo_carro(self):
        return "Este é um carro"

# Subclasse CarroEsportivo
class CarroEsportivo(Carro):
    def tipo_carro(self):
        return "Este é um carro esportivo"

# Subclasse CarroFamilia
class CarroFamilia(Carro):
    def tipo_carro(self):
        return "Este é um carro de família"

# Subclasse CarroSUV
class CarroSUV(Carro):
    def tipo_carro(self):
        return "Este é um carro SUV"

# Instanciando os objetos
carro = Carro()
carro_esportivo = CarroEsportivo()
carro_familia = CarroFamilia()
carro_suv = CarroSUV()

# Exibindo as mensagens
print(carro.tipo_carro())          # Saída: Este é um carro
print(carro_esportivo.tipo_carro()) # Saída: Este é um carro esportivo
print(carro_familia.tipo_carro())   # Saída: Este é um carro de família
print(carro_suv.tipo_carro())      # Saída: Este é um carro SUV
