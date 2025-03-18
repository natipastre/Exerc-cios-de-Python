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
