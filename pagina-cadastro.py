import tkinter.ttk
from tkinter import *
import datetime as dt 


lista_produtos = ['Arroz','Feijão','Macarrão','Farinha Branca','Farinha Dágua','Café','Açucar','Leite',
                  'Leite Integral','Carne de Gado','Peito de Frango','Carne Porco','Manteiga','Sal','Óleo',
                  'Azeite','Farinha de Trigo','Pão','Biscoito','Danone']

lista_tipos = ['Caixa','Unidade','Saco','Galão','Peso-1kg','Peso-500g']

lista_unidade = ['1','2','3','4','5','7','8','9','10','11','12','13','14','15','16','17','18','19','20','21','22',
                 '23','24','25','26','27','28','29','30']

lista_codigos = []


def salvar_dados():
    descricao = combobox_selecionar_produto.get()
    tipo = combobox_selecionar_tipo.get()
    quantidade = combobox_selecionar_quantidade.get()
    data_criacao = dt.datetime.now()
    data_criacao = data_criacao.strftime('%d/%m/%y %H:%M')
    codigo = len(lista_codigos)+1
    codigo_str = f'COD-{codigo}'
    lista_codigos.append((codigo_str, descricao, tipo, quantidade, data_criacao))
    str(print(lista_codigos))




janela = Tk()   # Criei uma janela (página de cadastro.)

# Título da Página
janela.title('Página de Cadastro')
janela.geometry("400x400")

texto_descricao = Label(janela, text='Decrição de todos os produtos')
texto_descricao.grid(column=0, row=1, padx=10, pady=10, sticky='nswe', columnspan=4)

combobox_selecionar_produto = tkinter.ttk.Combobox(values=lista_produtos)
combobox_selecionar_produto.grid(column=0, row=2, padx=10, pady=10, sticky='nswe', columnspan=4)

texto_tipo_unid = Label(text='Tipo da unidade do Produto -')
texto_tipo_unid.grid(column=0, row=3, padx=10, pady=10, sticky='nswe', columnspan=1)

combobox_selecionar_tipo = tkinter.ttk.Combobox(values=lista_tipos)
combobox_selecionar_tipo.grid(column=2, row=3, padx=10, pady=10, sticky='nswe', columnspan=1)

texto_quantidade = Label(text='Quantidade de unidades do Produto -')
texto_quantidade.grid(column=0, row=4, padx=10, pady=10, sticky='nswe', columnspan=1)

combobox_selecionar_quantidade = tkinter.ttk.Combobox(values=lista_unidade)
combobox_selecionar_quantidade.grid(column=2, row=4, padx=10, pady=10, sticky='nswe', columnspan=1)

botao_criar_codigo = tkinter.ttk.Button(text='Criar Código', command=salvar_dados)
botao_criar_codigo.grid(column=0, row=6, padx=10, pady=10, sticky='snwe', columnspan=4)


janela.mainloop()   # Aqui é o fim da janela (página de cadastro)
