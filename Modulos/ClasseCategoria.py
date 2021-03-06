#Depois de cadastrado o documento, as listBox devem ser limpadas.

from tkinter import *
from tkinter import ttk
from Modulos.Banco import *

class Categoria:

    def __init__(self):
        self.id = 0
        self.nome = ""

    def returnItensCategoria(self):
        """
        Este método tem como objetivo retornar todos os valores da Tabela Categoria
        :return: List com os valores
        """
        sql = "SELECT * FROM CATEGORIA order by nome;"
        result = dbSelect(sql)
        return result

    def returnIdCategoria(self, nome):
        sql = f"SELECT idCategoria FROM Categoria where nome = '{nome}'"
        result = dbSelect(sql)
        for item in result:
            return item[0]

    def returnNomeCategoria(self, idCategoria):
        sql = f"SELECT nome from Categoria where idCAtegoria = {idCategoria};"
        result = dbSelect(sql)
        return result[0]


    def addElementListBoxCadastroDoc(self, listbox=""):
        """
        Este método é responsável por preencher os valores da ListBox de categoria da Tela de Cadastro
        """
        listbox.delete(0, END)
        valores = self.returnItensCategoria()
        for item in valores:
            listbox.insert(END, item[1])

    def createNewCategoria(self, nome, individuoResponsavel, lb_itens):
        if nome == "" or individuoResponsavel == "":
            messagebox.showerror(title="Erro Cadastro Categoria", message="Por favor, verifique os valores informados!")
        else:
            sqlVerificaExistencia = f"SELECT * FROM Categoria where nome = '{nome}'"
            result = dbSelect(sqlVerificaExistencia)
            if result != []:
                messagebox.showerror(title="Erro Cadastro nova Categoria",
                                     message=f"Esta Categoria já foi cadastrado.\nPor favor, busque-a na lista acima!")
            else:
                sqlInstrucao = "INSERT INTO Categoria(nome, individuoResponsavel) values (?, ?);"
                sqlParametros = (nome, individuoResponsavel)
                dbInsert(sqlInstrucao, sqlParametros)
                messagebox.showinfo(title="Sucesso Cadastro de Categoria", message="Sua nova categoria foi cadastrada com sucesso")
                self.addElementListBoxCadastroDoc(lb_itens)

    def returnAllCategoria(self):
        sql = "SELECT nome from Categoria order by nome;"
        result = dbSelect(sql)
        categoriaList = []
        for item in result:
            categoriaList.append(item[0])

        return categoriaList

    def returnAutorCategoria(self, idCategoria):
        sql = f"SELECT individuoResponsavel from Categoria where idCategoria = '{idCategoria}'"
        result = dbSelect(sql)
        for item in result:
            return item[0]


