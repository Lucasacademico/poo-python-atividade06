from classes.veiculo import Veiculo

class Carro(Veiculo):
    def __init__(self, nome, ano, valor_diario, tipo_combustivel):
        super().__init__(nome, ano, valor_diario)
        self.__tipo_combustivel = tipo_combustivel

    @property
    def tipo_combustivel(self):
        return self.__tipo_combustivel

    @tipo_combustivel.setter
    def tipo_combustivel(self, valor):
        if not valor:
            raise ValueError("Combustível inválido")
        self.__tipo_combustivel = valor

    def desconto_dias(self, dias, porcentagem):
        valor_aluguel = super().calculo_aluguel(dias)
        if dias > 7:
            desconto_base = valor_aluguel - ((porcentagem / 100) * valor_aluguel)
            desconto_adicional_dias = desconto_base * 0.1
            resultado = desconto_base - desconto_adicional_dias
        else:
            resultado = super().desconto(dias, porcentagem)  # Chama o método normal se <= 7 dias
        return resultado
