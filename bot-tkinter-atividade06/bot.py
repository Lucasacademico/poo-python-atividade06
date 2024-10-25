from botcity.core import DesktopBot
from botcity.maestro import *
BotMaestroSDK.RAISE_NOT_CONNECTED = False

from classes.veiculo import Veiculo
from classes.carro import Carro
from classes.moto import Moto

import time

from dados import DataStorage

def main():
    maestro = BotMaestroSDK.from_sys_args()
    execution = maestro.get_execution()
    print(f"Task ID is: {execution.task_id}")
    print(f"Task Parameters are: {execution.parameters}")

    bot = DesktopBot()

    veiculos = []

    veiculo1 = Carro("Triton", 2013, 120.0, "Diesel")
    veiculos.append(veiculo1)
 
    veiculo2 = Moto("Harley", 2020, 150.0, 600)
    veiculos.append(veiculo2)

    dias_por_veiculo = {
        veiculo1.nome: 5,  # Triton terá 5 dias
        veiculo2.nome: 7   # Harley terá 7 dias
    }

    for veiculo in veiculos:
        if isinstance(veiculo, Carro):
            print(f"Carro criado: {veiculo.nome}, Ano: {veiculo.ano}, Valor Diário: R$ {veiculo.valor_diario}, Combustível: {veiculo.tipo_combustivel}")
        elif isinstance(veiculo, Moto):
            print(f"Moto criada: {veiculo.nome}, Ano: {veiculo.ano}, Valor Diário: R$ {veiculo.valor_diario}, Cilindrada: {veiculo.cilindrada}")
    
    ##### ALTERE O PATH DO CAMINHO
    app_path = r"C:\Users\lrand\OneDrive\Área de Trabalho\Atividades\atividade 06\bot-tkinter-atividade06\interface.py"
    # Launching the app
    bot.execute(app_path)

    for veiculo in veiculos:
        if not bot.find("campo_nome", matching=0.97, waiting_time=1000):
            not_found("campo_nome")
        bot.click_relative(640, 6)
        bot.paste(f'{veiculo.nome}')

        if not bot.find("campo_ano", matching=0.97, waiting_time=1000):
            not_found("campo_ano")
        bot.click_relative(609, 9)
        bot.paste(f'{veiculo.ano}')
        
        if not bot.find("campo_diaria", matching=0.97, waiting_time=1000):
            not_found("campo_diaria")
        bot.click_relative(622, 9)
        bot.paste(f'{veiculo.valor_diario}')

        if isinstance(veiculo, Carro):  # Se for carro, preenche combustível
            if not bot.find("campo_combustivel", matching=0.97, waiting_time=1000):
                not_found("campo_combustivel")
            bot.click_relative(654, 10)
            bot.paste(f'{veiculo.tipo_combustivel}')
        elif isinstance(veiculo, Moto):  # Se for moto, preenche cilindrada
            if not bot.find("campo_cilindrada", matching=0.97, waiting_time=1000):
                not_found("campo_cilindrada")
            bot.click_relative(655, 8)
            bot.paste(f'{veiculo.cilindrada}')
        
        if not bot.find("campo_dias", matching=0.97, waiting_time=1000):
            not_found("campo_dias")
        bot.click_relative(759, 13)
        bot.backspace()  # Limpa o campo
        bot.backspace()
        bot.backspace()
        bot.paste(str(dias_por_veiculo[veiculo.nome]))

        if not bot.find("botao_adicionar", matching=0.97, waiting_time=1000):
            not_found("botao_adicionar")
        bot.click()
        
        if not bot.find("botao_fechar_janela", matching=0.97, waiting_time=1000):
            not_found("botao_fechar_janela")
        bot.click()

    if not bot.find("verificar_aluguel", matching=0.97, waiting_time=1000):
        not_found("verificar_aluguel")
    bot.click()
    
    bot.wait(2000)
    bot.enter()   


def not_found(label):
    print(f"Element not found: {label}")

if __name__ == '__main__':
    main()
