import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk

class ConversorTemperatura:

    def __init__(self, master):
        self.master = master
        self.master.title('Conversor de Temperatura')
        self.master.geometry('400x250')
        self.master.resizable(False, False)
        self.master.iconbitmap('clear.png')

        # Cria o ícone e o título da janela
        self.imagem = Image.open('clear.png')
        self.imagem = self.imagem.resize((30, 30))
        self.icone = ImageTk.PhotoImage(self.imagem)
        self.master.iconphoto(False, self.icone)

        # Define o estilo de fonte
        self.fonte = ('Helvetica', 12)

        # Cria o rótulo de entrada
        self.label_entrada = ttk.Label(self.master, text='Digite a temperatura em Fahrenheit:', font=self.fonte)
        self.label_entrada.pack(pady=10)

        # Cria a entrada de temperatura
        self.entrada_temperatura = ttk.Entry(self.master, font=self.fonte)
        self.entrada_temperatura.pack()

        # Cria o botão de conversão
        self.botao_converter = ttk.Button(self.master, text='Converter', command=self.converter_temperatura)
        self.botao_converter.pack(pady=10)

        # Cria o botão de limpeza
        self.botao_limpar = ttk.Button(self.master, text='Limpar', command=self.limpar_temperatura)
        self.botao_limpar.pack(pady=5)

        # Cria a mensagem de erro
        self.mensagem_erro = ttk.Label(self.master, text='', foreground='red', font=self.fonte)
        self.mensagem_erro.pack(pady=10)

        # Cria o rótulo de saída
        self.label_saida = ttk.Label(self.master, text='Resultado:', font=self.fonte)
        self.label_saida.pack(pady=5)

        # Cria a saída de temperatura
        self.saida_temperatura = ttk.Label(self.master, text='', font=self.fonte)
        self.saida_temperatura.pack()

    def converter_temperatura(self):
        try:
            temperatura_fahrenheit = float(self.entrada_temperatura.get())
            temperatura_celsius = (temperatura_fahrenheit - 32) * 5/9
            self.saida_temperatura.config(text=f'{temperatura_celsius:.2f}')
            self.mensagem_erro.config(text='')
        except ValueError:
            self.mensagem_erro.config(text='Insira uma temperatura válida!')

    def limpar_temperatura(self):
        self.entrada_temperatura.delete(0, tk.END)
        self.saida_temperatura.config(text='')
        self.mensagem_erro.config(text='')

root = tk.Tk()
conversor = ConversorTemperatura(root)
root.mainloop()
