class Vendedor:
    def __init__(self, nome, id_vendedor):
        self.nome = nome
        self.id_vendedor = id_vendedor

    def exibir_vendedor(self):
        print(f"Vendedor: {self.nome:<20} | ID: {self.id_vendedor:>3}")


class Produto:
    def __init__(self, nome_produto, preco):
        self.nome_produto = nome_produto
        self.preco = preco

    def exibir_produto(self):
        print(f"Produto: {self.nome_produto:<30} | Preço: R$ {self.preco:>8.2f}")


def main():
    # Lista de vendedores
    lista_vendedores = [
        Vendedor("João", 1),
        Vendedor("Maria", 2),
        Vendedor("Pedro", 3)
    ]

    # Lista de produtos
    lista_produtos = [
        Produto("Teclado Mecânico ThunderKey", 499.90),
        Produto("Mouse Óptico DarkClaw", 249.90),
        Produto("Headset StormSound", 399.00),
        Produto("Monitor UltraWide DragonView", 1999.00),
        Produto("Cadeira Gamer ShadowSeat", 899.90),
        Produto("Mousepad RGB FireTrail", 149.90),
        Produto("Placa de Vídeo Inferno GTX", 3499.90),
        Produto("Controle DualForce Pro", 299.90),
        Produto("Microfone ThunderMic", 279.90),
        Produto("Webcam HD NightVision", 189.90)
    ]

    # Exibir vendedores
    print("---- Vendedores ----")
    for vendedor in lista_vendedores:
        vendedor.exibir_vendedor()

    # Exibir produtos
    print("\n---- Produtos ----")
    for produto in lista_produtos:
        produto.exibir_produto()

if __name__ == "__main__":
    main()
