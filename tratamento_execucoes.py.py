class NumeroNegativoException(Exception):
    def __init__(self, numero):
        super().__init__(f"O número {numero} é negativo. Por favor, digite um número positivo.")

def solicitar_numero():
    """NESTA LINHA FICA O TRY:"""
    numero = int(input("Digite um número inteiro positivo: "))
    if numero < 0:
        """NESTA LINHA FICA NumeroNegativoException"""        
    print(f"Você digitou o número {numero}.")        
"""NESTA LINHA FICA O ValueError"""  
"""NESTA LINHA FICA O PRINT PARA A EXCEPTION"""    
"""NESTA LINHA FICA O NumeroNegativoException"""
"""NESTA LINHA FICA O PRINT PARA A EXCEPTION"""   
    
solicitar_numero()

#try:
#raise NumeroNegativoException(numero)
#except ValueError:
#print("Erro: Entrada inválida. Por favor, digite um número inteiro.")
#except NumeroNegativoException as e:
#print(f"Erro: {e}")
