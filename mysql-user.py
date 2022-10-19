#Fazer uma ligação com o mysql, e criar novos usuários quando for
#utilizado o comando para criação de planilha.

#import mysql.connector
import hashlib
#import pygame
from tkinter import *
import tkinter as tk

entry = False

####################

janela = Tk()

largura = 200
altura = 100

larguraScreen = janela.winfo_screenwidth()
alturaScreen = janela.winfo_screenheight()

x = (larguraScreen/2) - (largura/2)
y = (alturaScreen/2) - (altura/2)


lb=Label(janela, text="Se identifique")
lb.place(x= 30, y=40)

#Label(janela, text="alguma coisa").pack()
lb1=Label(janela, text="E-mail")
ed1=Entry(janela)

lb2=Label(janela, text="Senha")
ed2=Entry(janela)

bt1=Button(janela, width=10, text="OK", command=janela.destroy)

lb.grid(row=0, column=1)
lb1.grid(row=1, column=0)
lb2.grid(row=2, column=0)
ed1.grid(row=1, column=1)
ed2.grid(row=2, column=1)
bt1.grid(row=3, column=1)


janela.title("Conta")
janela.geometry(f'{largura}x{altura}+{x:.0f}+{y:.0f}')
janela.mainloop()

########################

if entry is True:
    class tela_de_login():
        print('Bem-vindo')
if entry is False:
    print('Senha incorreta')

class createaccount():
    def some_function(argument1):
        """ Cria a conta automaticamente usando as informações necessárias
        
        É preciso de login, e senha que sera enviada para o BD
        para então armazenar valores de MD5 HASH unidirecionais
        """
        input('')
        pass
