import ttkbootstrap as ttk
from ttkbootstrap.constants import *

janela = ttk.Window(themename="superhero")
janela.title('Window')
janela.geometry('500x500')
input_entry1 = ttk.Entry(janela, width = 5)
input_entry1.grid(row = 2, column = 2 , padx = 10)
b1 = ttk.Button(janela, text="Submit", bootstyle="success")
b1.pack(side=LEFT, padx=215, pady=100)



def mostrar_altura():
    n1 = float(input_entry1.get())
    n2 = float(input_entry2.get()) 





janela.mainloop()