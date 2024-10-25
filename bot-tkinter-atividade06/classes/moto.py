from classes.veiculo import Veiculo


class Moto(Veiculo):
    def __init__(self, nome, ano, valor_diario, cilindrada):
        super().__init__(nome, ano, valor_diario)
        self._cilindrada = cilindrada  # Alterado para um único underscore

    @property
    def cilindrada(self):
        return self._cilindrada  # Acessa o atributo corretamente
    
    @cilindrada.setter
    def cilindrada(self, valor):
        if not valor:
            raise ValueError("Valor inválido")
        self._cilindrada = valor  # Atribui corretamente ao atributo

    def calculo_aluguel_moto(self, dias, cilindradas):
        aluguel = super().calculo_aluguel(dias)
        if cilindradas > 200:      
            adicional_cc = (aluguel / 100) * 10
            resultado = aluguel + adicional_cc
        else:
            resultado = aluguel
        return resultado

