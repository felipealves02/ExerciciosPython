import datetime
from tkinter import *




    # texto_resposta['text'] = print(data_atual)

janela =Tk()
janela.title("Ciclo Menstrual" )

janela.geometry("500x500")

texto_orientacao = Label(janela, text="Você menstruou hoje? Clique no botão para ver seu ciclo menstrual.")
texto_orientacao.grid(column=0, row=0, padx=10, pady=10)


def calcular_data():
    data_atual = datetime.date.today()
    data_limite = data_atual + datetime.timedelta(days=3*365)
    data_futura = data_atual + datetime.timedelta(days=28)
    # print(f'Data atual:{data_atual}')
    # print(f'Data daqui a 28 dias:{data_futura}')
    # print(f'Data limite {data_limite}')

    # data = data_atual
    while data_atual <= data_limite:
        data_atual += datetime.timedelta(days= 28)
        data_atual.set(f'{data_atual}')
        
botao = Button(janela, text="SIM", command=calcular_data)
botao.grid(column=0, row=1, padx=10, pady=10)

texto_resposta = Label(janela, text="")
texto_resposta.grid(column=0, row=2, padx=20, pady=20)


janela.mainloop()
