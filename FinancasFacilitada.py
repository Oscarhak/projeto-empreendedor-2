from tkinter import *
import tkinter as tk
from pip._vendor import requests

class Interface:
    principal = tk.Tk()
    principal.title("Finanças Facilitadas")
    principal.geometry("550x290")
    principal.configure(bg='#FFFFFF')

class Frames:

    frameJurosCompostos = Frame(Interface.principal,
                              width=550,
                              height=290,
                              bg='#ededed',
                              highlightbackground='#ffffff',
                              highlightthickness=0)

    frameJurosCompostos.place(x=0, y=0)

class label:

    cifrao = PhotoImage(file='imagens\\faculRS.png')
    porcentagem = PhotoImage(file='imagens\\faculPorcent.png')
    relogio = PhotoImage(file='imagens\\faculClock.png')
    aviso = PhotoImage(file='imagens\\aviso.png')
    aporteIcon = PhotoImage(file='imagens\\faculAporte.png')
    frameResultado = PhotoImage(file='imagens\\frameResultado.png')

    labelTitulo = Label(Frames.frameJurosCompostos,
                       text="Simulador de Juros compostos",
                        font=('Finance', 16),
                       foreground='#000000',
                       bg='#ededed')

    labelValor = Label(Frames.frameJurosCompostos,
                        text="Valor inicial aplicado",
                       font=('Finance', 9),
                        foreground='#000000',
                        bg='#ededed')
    labelCifrao = Label(Frames.frameJurosCompostos,
                        image=cifrao)

    labelTaxa = Label(Frames.frameJurosCompostos,
                       text="Taxa de juros",
                      font=('Finance', 9),
                       foreground='#000000',
                       bg='#ededed')
    labelPorcentagem = Label(Frames.frameJurosCompostos,
                        image=porcentagem)

    labelTempo = Label(Frames.frameJurosCompostos,
                      text="Periodo",
                       font=('Finance', 9),
                      foreground='#000000',
                      bg='#ededed')
    labelRelogio = Label(Frames.frameJurosCompostos,
                        image=relogio)

    labelFrameResultado = Label(Frames.frameJurosCompostos,
                        image=frameResultado)
    labelResultado = Label(labelFrameResultado,
                        text="",
                        font=('Finance', 16),
                        foreground='#000000',
                        bg='#ffffff')

    labelTotal = Label(Frames.frameJurosCompostos,
                       text="Valor total final",
                       font=('Finance', 9),
                       foreground='#000000',
                       bg='#ededed')

    labelFundoAviso = Label(Interface.principal,
                       bg='#ededed',
                      image=aviso)
    labelAviso = Label(labelFundoAviso,
                            text="",
                            font=('Finance', 10),
                            foreground='#000000',
                            bg='#ffffff')

    labelAporte = Label(Frames.frameJurosCompostos,
                        text="Aportes mensais",
                        font=('Finance', 9),
                        foreground='#000000',
                        bg='#ededed')
    labelAporteIcon = Label(Interface.principal,
                            bg='#ededed',
                            image=aporteIcon)

    labelTitulo.place(x=20, y=20)
    labelValor.place(x=20, y=60)
    labelTaxa.place(x=200, y=60)
    labelTempo.place(x=380, y=60)
    labelTotal.place(x=50, y=170)
    labelAporte.place(x=20, y=115)
    labelFrameResultado.place(x=23, y=190)

class entry:

    entryValor = Entry(Frames.frameJurosCompostos,
                        relief=FLAT)

    entryTaxa = Entry(Frames.frameJurosCompostos,
                        relief=FLAT)

    entryTempo = Entry(Frames.frameJurosCompostos,
                        relief=FLAT)

    entryAporte = Entry(Frames.frameJurosCompostos,
                        relief=FLAT)

    label.labelCifrao.place(x=20, y=85)
    entryValor.place(x=46, y=90)
    label.labelPorcentagem.place(x=198, y=86)
    entryTaxa.place(x=222, y=90)
    label.labelRelogio.place(x=376, y=86)
    entryTempo.place(x=400, y=90)
    label.labelAporteIcon.place(x=18, y=135)
    entryAporte.place(x=46, y=140)

class Button:

    calcular=PhotoImage(file='imagens\\faculCalcular.png')
    limpar = PhotoImage(file='imagens\\faculLimpar.png')
    fechar = PhotoImage(file='imagens\\botao-x.png')
    cotacao = PhotoImage(file='imagens\\faculCotacao.png')

    buttonCalc = Button(Frames.frameJurosCompostos,
                        image=calcular,
                        command=lambda: Funcoes.calcular(self=None),
                        bg='#ededed',
                        bd=0)

    buttonLimpar = Button(Frames.frameJurosCompostos,
                        image=limpar,
                          command=lambda: Funcoes.limpar(self=None),
                        bg='#ededed',
                        bd=0)

    buttonfechar = Button(label.labelFundoAviso,
                          image=fechar,
                          command=lambda: Funcoes.fechar(self=None),
                          bg='#ffffff',
                          bd=0)

    buttonCotacao = Button(Interface.principal,
                          image=cotacao,
                          command=lambda: Funcoes.cotacao(self=None),
                          bg='#ededed',
                          bd=0)

    buttonCalc.place(x=350, y=140)
    buttonLimpar.place(x=440, y=140)
    buttonCotacao.place(x=460, y=10)

periodoEscolhido=IntVar()
taxaEscolhida=IntVar()

class CheckButton:

    checkbuttonPeriodoM = Checkbutton(Frames.frameJurosCompostos,
                                      text="mensal",
                                      variable=periodoEscolhido,
                                      onvalue=1,
                                      offvalue=0)

    checkbuttonPeriodoA = Checkbutton(Frames.frameJurosCompostos,
                                      text="anual",
                                      variable=periodoEscolhido,
                                      onvalue=2,
                                      offvalue=0)

    checkbuttonTaxaM = Checkbutton(Frames.frameJurosCompostos,
                                      text="mensal",
                                      variable=taxaEscolhida,
                                      onvalue=3,
                                      offvalue=0)

    checkbuttonTaxaA = Checkbutton(Frames.frameJurosCompostos,
                                      text="anual",
                                      variable=taxaEscolhida,
                                      onvalue=4,
                                      offvalue=0)

    checkbuttonPeriodoM.place(x=440, y=109)
    checkbuttonPeriodoA.place(x=385, y=109)
    checkbuttonTaxaM.place(x=280, y=109)
    checkbuttonTaxaA.place(x=225, y=109)

class Funcoes:

    def calcular(self):

        if entry.entryValor.get() == "":

            label.labelFundoAviso.place(x=180, y=45)
            label.labelAviso['text'] = "O campo\nValor inicial aplicado,\nnão foi preenchido."
            label.labelAviso.place(x=15, y=15)
            Button.buttonfechar.place(x=3.5, y=3.5)

        elif entry.entryTaxa.get() == "":

            label.labelFundoAviso.place(x=180, y=45)
            label.labelAviso['text'] = "O campo\nValor taxa de juros,\nnão foi preenchido."
            label.labelAviso.place(x=20, y=15)
            Button.buttonfechar.place(x=3.5, y=3.5)

        elif entry.entryTempo.get() == "":

            label.labelFundoAviso.place(x=180, y=45)
            label.labelAviso['text'] = "O campo\nValor periodo em anos,\nnão foi preenchido."
            label.labelAviso.place(x=13, y=15)
            Button.buttonfechar.place(x=3.5, y=3.5)

        elif taxaEscolhida.get() == 0:

            label.labelFundoAviso.place(x=180, y=45)
            label.labelAviso['text'] = "O periodo da taxa\n precisa ser selecionado"
            label.labelAviso.place(x=8, y=23)
            Button.buttonfechar.place(x=3.5, y=3.5)

        elif periodoEscolhido.get() == 0:

            label.labelFundoAviso.place(x=180, y=45)
            label.labelAviso['text'] = "O periodo precisa ser\nselecionado como\nmensal ou anual"
            label.labelAviso.place(x=16, y=19)
            Button.buttonfechar.place(x=3.5, y=3.5)

        else:

            valor = float(entry.entryValor.get())
            taxa = float(entry.entryTaxa.get())
            tempo = float(entry.entryTempo.get())

            if entry.entryAporte.get() != "":

                aporte = float(entry.entryAporte.get())

                if taxaEscolhida.get() == 3: #Taxa mensal

                    if periodoEscolhido.get() == 1: #Periodo mensal

                        resultadoValorInicial = valor*(((taxa/100)+1)**tempo)
                        resultadoValorAporte = aporte * ((((taxa / 100) + 1) ** tempo)-1) / (taxa / 100)
                        resultado = resultadoValorInicial + resultadoValorAporte

                    else: #Periodo anual

                        resultadoValorInicial = valor*(((taxa/100)+1)**(tempo*12))
                        resultadoValorAporte = aporte * ((((taxa / 100) + 1) ** (tempo*12))-1) / (taxa / 100)
                        resultado = resultadoValorInicial + resultadoValorAporte

                else: #Taxa anual

                    if periodoEscolhido.get() == 2: #Periodo anual

                        taxaMensal = ((taxa / 100) + 1) ** (1 / 12)
                        resultadoValorInicial = valor*(((taxa/100)+1)**tempo)
                        resultadoValorAporte = aporte * (((taxaMensal) ** (tempo*12))-1) / (taxaMensal-1)
                        resultado = resultadoValorInicial + resultadoValorAporte

                    else: #Periodo mensal

                        taxaMensal = ((taxa/100)+1)**(1/12)
                        resultadoValorInicial = valor*(taxaMensal)**tempo
                        resultadoValorAporte = aporte*(((taxaMensal**tempo)-1)/(taxaMensal-1))
                        resultado = resultadoValorInicial+resultadoValorAporte


                label.labelResultado['text'] = "R$ %.2f" % resultado
                label.labelResultado.place(x=100, y=16)


            else:

                if taxaEscolhida.get() == 3:

                    if periodoEscolhido.get() == 1:

                        resultado = valor*(((taxa/100)+1)**tempo)

                    else:

                        resultado = valor*(((taxa/100)+1)**(tempo*12))

                else:

                    if periodoEscolhido.get() == 2:

                        resultado = valor*(((taxa/100)+1)**tempo)

                    else:

                        taxaFinal = ((taxa/100)+1)**(1/12)
                        resultado = valor*(taxaFinal)**tempo

                label.labelResultado['text'] = "R$ %.2f" % resultado
                label.labelResultado.place(x=100, y=16)

    def limpar(self):

        entry.entryTaxa.delete(0, END)
        entry.entryValor.delete(0, END)
        entry.entryTempo.delete(0, END)
        entry.entryAporte.delete(0, END)
        entry.entryValor.focus_force()
        label.labelResultado['text'] = ""
        CheckButton.checkbuttonPeriodoM.deselect()
        CheckButton.checkbuttonPeriodoA.deselect()
        CheckButton.checkbuttonTaxaM.deselect()
        CheckButton.checkbuttonTaxaA.deselect()

    def fechar(self):

        label.labelFundoAviso.place_forget()
        Button.buttonfechar.place_forget()

    def cotacao(self):

        req = requests.get("https://economia.awesomeapi.com.br/last/USD-BRL,EUR-BRL,BTC-BRL")

        req_dic = req.json()

        cotacao_usd = req_dic['USDBRL']['bid']
        cotacao_eur = req_dic['EURBRL']['bid']
        cotacao_btc = req_dic['BTCBRL']['bid']
        cotacao_btc_float = float(cotacao_btc)*1000

        label.labelFundoAviso.place(x=180, y=45)
        label.labelAviso['text'] = 'Dolar: R$',cotacao_usd,'\n Euro: R$',cotacao_eur,'\n Bitcoin: R$',cotacao_btc_float
        label.labelAviso.place(x=33, y=21)
        Button.buttonfechar.place(x=3.5, y=3.5)


Interface.principal.mainloop()