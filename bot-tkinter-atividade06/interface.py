import tkinter as tk
from tkinter import messagebox, ttk
from classes.carro import Carro
from classes.moto import Moto

# Funções para adicionar veículo e calcular aluguel
veiculos = []

def adicionar_veiculo():
    nome = entry_nome.get()
    ano = entry_ano.get()
    valor_diario = entry_valor_diario.get()
    tipo_combustivel = entry_combustivel.get()
    cilindrada = entry_cilindrada.get()

    if nome and ano and valor_diario:
        # Verifica se a cilindrada foi fornecida e é maior que zero
        if cilindrada and int(cilindrada) > 0:
            veiculo = Moto(nome, ano, float(valor_diario), int(cilindrada))
            tipo_veiculo = "Moto"
        else:
            veiculo = Carro(nome, ano, float(valor_diario), tipo_combustivel)
            tipo_veiculo = "Carro"
        
        veiculos.append(veiculo)
        messagebox.showinfo("Sucesso", f"Veículo '{veiculo.nome}' adicionado como {tipo_veiculo}!")

        # Atualiza a Treeview com o novo veículo
        tree.insert("", "end", values=(
            veiculo.nome,
            veiculo.ano,
            valor_diario,
            tipo_combustivel if tipo_veiculo == "Carro" else "N/A",
            cilindrada if tipo_veiculo == "Moto" else "N/A"
        ))

        # Limpa os campos de entrada
        entry_nome.delete(0, tk.END)
        entry_ano.delete(0, tk.END)
        entry_valor_diario.delete(0, tk.END)
        entry_combustivel.delete(0, tk.END)
        entry_cilindrada.delete(0, tk.END)
    else:
        messagebox.showerror("Erro", "Preencha todos os campos obrigatórios.")


def calcular_aluguel():
    dias = entry_dias.get()
    if dias.isdigit() and veiculos:
        dias = int(dias)
        resultados = []
        for veiculo in veiculos:
            if isinstance(veiculo, Moto):
                aluguel = veiculo.calculo_aluguel_moto(dias, veiculo.cilindrada)
            else:
                aluguel = veiculo.calculo_aluguel(dias)
            resultados.append(f"{veiculo.nome}: R${aluguel:.2f}")

        messagebox.showinfo("Aluguel Calculado", "\n".join(resultados))
    else:
        messagebox.showerror("Erro", "Preencha o número de dias e adicione um veículo.")

# Configuração da janela principal
root = tk.Tk()
root.title("Gerenciador de Veículos")
root.state('zoomed')  # Para maximizar a janela


# Campos de entrada
tk.Label(root, text="Nome do Veículo:").grid(row=0, column=0)
entry_nome = tk.Entry(root)
entry_nome.grid(row=0, column=1)

tk.Label(root, text="Ano:").grid(row=1, column=0)
entry_ano = tk.Entry(root)
entry_ano.grid(row=1, column=1)

tk.Label(root, text="Valor Diário:").grid(row=2, column=0)
entry_valor_diario = tk.Entry(root)
entry_valor_diario.grid(row=2, column=1)

tk.Label(root, text="Tipo de Combustível:").grid(row=3, column=0)
entry_combustivel = tk.Entry(root)
entry_combustivel.grid(row=3, column=1)

tk.Label(root, text="Cilindrada (se moto):").grid(row=4, column=0)
entry_cilindrada = tk.Entry(root)
entry_cilindrada.grid(row=4, column=1)

tk.Label(root, text="Número de Dias:").grid(row=5, column=0)
entry_dias = tk.Entry(root)
entry_dias.grid(row=5, column=1)

# Botões
btn_adicionar = tk.Button(root, text="Adicionar Veículo", command=adicionar_veiculo)
btn_adicionar.grid(row=6, column=0)

btn_calcular = tk.Button(root, text="Calcular Aluguel", command=calcular_aluguel)
btn_calcular.grid(row=6, column=1)

# Configuração da Treeview
columns = ("Nome", "Ano", "Valor Diário", "Tipo de Combustível", "Cilindrada")
tree = ttk.Treeview(root, columns=columns, show="headings")

# Centraliza o texto nas colunas
for col in columns:
    tree.heading(col, text=col)
    tree.column(col, anchor="center")

tree.grid(row=7, column=0, columnspan=2)

# Iniciar a interface
root.mainloop()




# import tkinter as tk
# from tkinter import messagebox, ttk

# from classes.veiculo import Veiculo
# from classes.carro import Carro
# from classes.moto import Moto

# import tkinter as tk
# from tkinter import messagebox, ttk


# # Configuração da janela principal
# root = tk.Tk()
# root.title("Gerenciador de Veículos")
# root.state('zoomed') 

# # Campos de entrada
# tk.Label(root, text="Nome do Veículo:").grid(row=0, column=0)
# entry_nome = tk.Entry(root)
# entry_nome.grid(row=0, column=1)

# tk.Label(root, text="Ano:").grid(row=1, column=0)
# entry_ano = tk.Entry(root)
# entry_ano.grid(row=1, column=1)

# tk.Label(root, text="Valor Diário:").grid(row=2, column=0)
# entry_valor_diario = tk.Entry(root)
# entry_valor_diario.grid(row=2, column=1)

# tk.Label(root, text="Tipo de Combustível:").grid(row=3, column=0)
# entry_combustivel = tk.Entry(root)
# entry_combustivel.grid(row=3, column=1)

# tk.Label(root, text="Número de Dias:").grid(row=4, column=0)
# entry_dias = tk.Entry(root)
# entry_dias.grid(row=4, column=1)

# # Criação da tabela
# columns = ("Nome", "Ano", "Valor Diário")
# tree = ttk.Treeview(root, columns=columns, show="headings")
# tree.grid(row=6, column=0, columnspan=2)

# for col in columns:
#     tree.heading(col, text=col)
#     tree.column(col, anchor="center")

# # Lista para armazenar veículos
# veiculos = []

# def adicionar_veiculo():
#     nome = entry_nome.get()
#     ano = entry_ano.get()
#     valor_diario = entry_valor_diario.get()
    
#     # Adiciona o veículo na lista
#     veiculo = Carro(nome, ano, float(valor_diario), entry_combustivel.get())
#     veiculos.append(veiculo)

#     # Atualiza a tabela
#     tree.insert("", "end", values=(veiculo.nome, veiculo.ano, veiculo.valor_diario))

#     # Limpa os campos
#     entry_nome.delete(0, tk.END)
#     entry_ano.delete(0, tk.END)
#     entry_valor_diario.delete(0, tk.END)
#     entry_combustivel.delete(0, tk.END)

# def calcular_aluguel():
#     dias = entry_dias.get()
#     if veiculos:
#         veiculo = veiculos[-1]  # Exemplo: pega o último veículo adicionado
#         try:
#             aluguel = veiculo.calculo_aluguel(int(dias))
#             messagebox.showinfo("Resultado do Aluguel", f"Valor do aluguel: R$ {aluguel:.2f}")
#         except ValueError as e:
#             messagebox.showerror("Erro", str(e))
#     else:
#         messagebox.showwarning("Aviso", "Nenhum veículo cadastrado.")

# # Botões
# btn_adicionar = tk.Button(root, text="Adicionar Veículo", command=adicionar_veiculo)
# btn_adicionar.grid(row=5, column=0)

# btn_calcular = tk.Button(root, text="Calcular Aluguel", command=calcular_aluguel)
# btn_calcular.grid(row=5, column=1)

# # Iniciar a interface
# root.mainloop()



