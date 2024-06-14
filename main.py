#janela => 500 x 500
#título
#campos para selecionar as moedas de origem e destino 
#botão para converter
#lista de exibição com os nomes das moedas 

#importar a biblioteca que vai fazer a janela 
import customtkinter

#criar e configurar a janela
customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("blue")

janela = customtkinter.CTk()
janela.geometry("600x600")

#criar os botões, textos e demais elementos 
titulo = customtkinter.CTkLabel(janela, text="Conversor de Moedas", font=("Times New Roman", 25), text_color="#EA7EE7")
texto_moeda_origem = customtkinter.CTkLabel(janela, text="Selecione a moeda de origem", font=("Times New Roman", 19))
texto_moeda_destino = customtkinter.CTkLabel(janela, text="Selecione a moeda de destino", font=("Times New Roman", 19))
campo_moeda_origem = customtkinter.CTkOptionMenu(janela, values=["USD", "EUR", "BRL", "BTC"], font=("Times New Roman", 13), fg_color="#EA7EE7", text_color="black")
campo_moeda_destino = customtkinter.CTkOptionMenu(janela, values=["USD", "EUR", "BRL", "BTC"], font=("Times New Roman", 13), fg_color="#EA7EE7", text_color="black")

def converter_moeda():
    print("Converter moeda")

botao_converter = customtkinter.CTkButton(janela, text="Converter", command=converter_moeda, font=("Times New Roman", 17), fg_color="#EA7EE7", text_color="black")

lista_moedas = customtkinter.CTkScrollableFrame(janela)

moedas_disponiveis = ["USD = Dólar americano", "EUR = Euro",  "BRL = Real brasileiro", "BTC = Bitcoin"]

for moeda in moedas_disponiveis:
    texto_moeda = customtkinter.CTkLabel(lista_moedas, text= moeda, font=("Times New Roman", 15))
    texto_moeda.pack()

#moeda1 = customtkinter.CTkLabel(lista_moedas, text="USD = Dólar americano")
#moeda2 = customtkinter.CTkLabel(lista_moedas, text="EUR = Euro")
#moeda3 = customtkinter.CTkLabel(lista_moedas, text="BRL = Real brasileiro")
#moeda4 = customtkinter.CTkLabel(lista_moedas, text="BTC = Bitcoin")
#moeda1.pack()
#moeda2.pack()
#moeda3.pack()
#moeda4.pack()

#colocar os elementos criados na tela 
titulo.pack(padx=10, pady=10)
texto_moeda_origem.pack(padx=4, pady=4)
campo_moeda_origem.pack(padx=4, pady=4)
texto_moeda_destino.pack(padx=4, pady=4)
campo_moeda_destino.pack(padx=4, pady=4)
botao_converter.pack(padx=13, pady=13)
lista_moedas.pack(padx=10, pady=10)

#rodar a janela 
janela.mainloop()