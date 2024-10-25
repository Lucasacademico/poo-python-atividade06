class Veiculo:
    quantidade_veiculo = 0

    def __init__(self, nome, ano, valor_diario):
        self.__nome = nome
        self.__ano = ano 
        self.__valor_diario = valor_diario
        Veiculo.quantidade_veiculo += 1

    @property
    def nome(self):
        return self.__nome
    
    @nome.setter
    def nome(self, valor):
        if not valor:
            raise ValueError("Nome inválido")
        self.__nome = valor

    @property
    def ano(self):
        return self.__ano
    
    @ano.setter
    def ano(self, valor):
        if not valor:
            raise ValueError("Ano inválido")
        self.__ano = valor

    @property
    def valor_diario(self):
        return self.__valor_diario
    
    @valor_diario.setter
    def valor_diario(self, valor):
        if not valor:
            raise ValueError("Valor diário deve ser maior que zero")
        self.__valor_diario = valor

    def calculo_aluguel(self, dias, cupom=0):
        if dias <= 0:
            raise ValueError("O número de dias deve ser maior que zero.")
        aluguel = dias * self.__valor_diario
        if cupom:
            aluguel -= aluguel * (cupom / 100)
        return aluguel
    
    def desconto(self, dias, porcentagem):
        if not (0 <= porcentagem <= 100):
            raise ValueError("A porcentagem deve estar entre 0 e 100.")
        aluguel = self.calculo_aluguel(dias)  # Chamando calculo_aluguel diretamente
        valor_desconto = (porcentagem / 100) * aluguel
        resultado = aluguel - valor_desconto
        return resultado

    
    @classmethod
    def obter_quantidade_veiculos(cls):
        return cls.quantidade_veiculo



    






    


