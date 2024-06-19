#janela => 500 x 500
#título
#campos para selecionar as moedas de origem e destino 
#botão para converter
#lista de exibição com os nomes das moedas 

#importar a biblioteca que vai fazer a janela 
import customtkinter
from pegar_moedas import nomes_moedas, conversoes_disponiveis
from pegar_cotacao import pegar_cotacao_moeda

#criar e configurar a janela
customtkinter.set_appearance_mode("light")
customtkinter.set_default_color_theme("blue")

janela = customtkinter.CTk()
janela.geometry("600x600")
janela.title("Conversor de moedas")
janela.iconbitmap("despesas.ico")

dic_conversoes_disponiveis = conversoes_disponiveis()

#criar os botões, textos e demais elementos 
titulo = customtkinter.CTkLabel(janela, text="Conversor de Moedas", font=("Times New Roman", 25), text_color="#E700FA")
texto_moeda_origem = customtkinter.CTkLabel(janela, text="Selecione a moeda de origem", font=("Times New Roman", 19))
texto_moeda_destino = customtkinter.CTkLabel(janela, text="Selecione a moeda de destino", font=("Times New Roman", 19))

def carregar_moedas_destino(moeda_selecionada):
    lista_moedas_destino = dic_conversoes_disponiveis[moeda_selecionada]
    campo_moeda_destino.configure(values = lista_moedas_destino)
    campo_moeda_destino.set(lista_moedas_destino[0])

campo_moeda_origem = customtkinter.CTkOptionMenu(janela, values=list(dic_conversoes_disponiveis.keys()), command= carregar_moedas_destino, font=("Times New Roman", 13), fg_color="#EA7EE7", text_color="black")
campo_moeda_destino = customtkinter.CTkOptionMenu(janela, values=["Selecione uma moeda de origem"], font=("Times New Roman", 13), fg_color="#EA7EE7", text_color="black")

def converter_moeda():
    moeda_origem = campo_moeda_origem.get()
    moeda_destino = campo_moeda_destino.get()
    if moeda_origem and moeda_destino: 
        cotacao = pegar_cotacao_moeda(moeda_origem, moeda_destino)
        texto_cotacao_moeda.configure(text=f"1 {moeda_origem} = {cotacao} {moeda_destino}")


botao_converter = customtkinter.CTkButton(janela, text="Converter", command=converter_moeda, font=("Times New Roman", 17), fg_color="#EA7EE7", text_color="black")

lista_moedas = customtkinter.CTkScrollableFrame(janela)

texto_cotacao_moeda = customtkinter.CTkLabel(janela, text="", font= ("Times New Roman", 16), fg_color="#F5B1FA")

#moedas_disponiveis = ["USD = Dólar americano", "EUR = Euro",  "BRL = Real brasileiro", "BTC = Bitcoin"]
moedas_disponiveis = nomes_moedas()

for codigo_moeda in moedas_disponiveis:
    nome_moeda = moedas_disponiveis[codigo_moeda]
    texto_moeda = customtkinter.CTkLabel(lista_moedas, text=f"{codigo_moeda}: {nome_moeda}", font=("Times New Roman", 15))
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
texto_cotacao_moeda.pack(padx=10, pady=10)
lista_moedas.pack(padx=10, pady=10)

#rodar a janela 
janela.mainloop()