import ttkbootstrap as ttk
from ttkbootstrap.constants import *

# Inicialização da janela
janela = ttk.Window(themename="superhero")
janela.title('Cálculo do IMC')
janela.geometry('500x500')

# Label e entrada para o peso
label_peso = ttk.Label(janela, text='Digite seu Peso (kg): ')
label_peso.grid(row=0, column=0, padx=21, pady=10)

input_entry_peso = ttk.Entry(janela)
input_entry_peso.grid(row=0, column=1, padx=21, pady=10)

# Label e entrada para a altura
label_altura = ttk.Label(janela, text='Digite sua Altura (m): ')
label_altura.grid(row=1, column=0, padx=21, pady=10)

input_entry_altura = ttk.Entry(janela)
input_entry_altura.grid(row=1, column=1, padx=21, pady=10)

# Função para calcular e mostrar o IMC
def mostrar_IMC():
    try:
        # Recupera o peso e a altura das entradas
        peso = float(input_entry_peso.get())
        altura = float(input_entry_altura.get())

        # Calcula o IMC
        imc = peso / (altura ** 2)
        
        # Exibe o resultado no label
        resultado_label.config(text=f'Seu IMC é: {imc:.2f}')
    except ValueError:
        # Se a entrada não for um número válido
        resultado_label.config(text='Por favor, insira números válidos.')

# Botão para calcular o IMC
b1 = ttk.Button(janela, text="Calcular IMC", bootstyle="success", command=mostrar_IMC)
b1.grid(row=2, column=1, pady=20)

# Label para mostrar o resultado do IMC
resultado_label = ttk.Label(janela, text='')
resultado_label.grid(row=3, column=1, pady=30)

# Inicia a janela principal
janela.mainloop()
