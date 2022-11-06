from tkinter import *
import tkinter as tk

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

    frameResultado = Frame(Interface.principal,
                                width=450,
                                height=60,
                                bg='#ffffff',
                                highlightbackground='#ffffff',
                                highlightthickness=0)

    frameAviso = Frame(Interface.principal,
                           width=180,
                           height=90,
                           bg='#ffffff',
                           highlightthickness=0)

    frameJurosCompostos.place(x=0, y=0)
    frameResultado.place(x=50, y=200)

class label:

    cifrao = PhotoImage(file='imagens\\faculRS.png')
    porcentagem = PhotoImage(file='imagens\\faculPorcent.png')

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

    labelResultado = Label(Frames.frameResultado,
                        text="",
                        font=('Finance', 16),
                        foreground='#000000',
                        bg='#ffffff')

    labelTotal = Label(Frames.frameJurosCompostos,
                       text="Valor total final",
                       font=('Finance', 9),
                       foreground='#000000',
                       bg='#ededed')

    labelErro = Label(Frames.frameAviso,
                       text="",
                       font=('Finance', 10),
                       foreground='#000000',
                       bg='#ffffff')

    labelTitulo.place(x=20, y=20)
    labelValor.place(x=20, y=60)
    labelTaxa.place(x=200, y=60)
    labelTempo.place(x=380, y=60)
    labelTotal.place(x=50, y=170)
    labelErro.place(x=10, y=20)

class entry:

    entryValor = Entry(Frames.frameJurosCompostos)

    entryTaxa = Entry(Frames.frameJurosCompostos)

    entryTempo = Entry(Frames.frameJurosCompostos)

    label.labelCifrao.place(x=20, y=83)
    entryValor.place(x=46, y=90)
    label.labelPorcentagem.place(x=200, y=83)
    entryTaxa.place(x=222, y=90)
    entryTempo.place(x=380, y=90)

class Button:

    calcular=PhotoImage(file='imagens\\faculCalcular.png')
    limpar = PhotoImage(file='imagens\\faculLimpar.png')
    fechar = PhotoImage(file='imagens\\botao-x.png')

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

    buttonfechar = Button(Interface.principal,
                          image=fechar,
                          command=lambda: Funcoes.fechar(self=None),
                          bg='#ededed',
                          bd=0)

    buttonCalc.place(x=350, y=140)
    buttonLimpar.place(x=440, y=140)

    # ff9900

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

            Frames.frameAviso.place(x=180, y=50)
            label.labelErro['text'] = "O campo\nValor inicial aplicado,\nnão foi preenchido."
            Button.buttonfechar.place(x=180, y=50)

        elif entry.entryTaxa.get() == "":

            Frames.frameAviso.place(x=180, y=50)
            label.labelErro['text'] = "O campo\nValor taxa de juros,\nnão foi preenchido."
            Button.buttonfechar.place(x=180, y=50)

        elif entry.entryTempo.get() == "":

            Frames.frameAviso.place(x=180, y=50)
            label.labelErro['text'] = "O campo\nValor periodo em anos,\nnão foi preenchido."
            Button.buttonfechar.place(x=180, y=50)

        elif taxaEscolhida.get() == 0:

            Frames.frameAviso.place(x=180, y=50)
            label.labelErro['text'] = "O periodo da taxa\n precisa ser selecionado"
            Button.buttonfechar.place(x=180, y=50)

        elif periodoEscolhido.get() == 0:

            Frames.frameAviso.place(x=180, y=50)
            label.labelErro['text'] = "O periodo precisa ser\nselecionado como\nmensal ou anual"
            Button.buttonfechar.place(x=180, y=50)

        else:

            valor = int(entry.entryValor.get())
            taxa = int(entry.entryTaxa.get())
            tempo = int(entry.entryTempo.get())

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
        entry.entryValor.focus_force()
        label.labelResultado['text'] = ""
        CheckButton.checkbuttonPeriodoM.deselect()
        CheckButton.checkbuttonPeriodoA.deselect()
        CheckButton.checkbuttonTaxaM.deselect()
        CheckButton.checkbuttonTaxaA.deselect()

    def fechar(self):

        Frames.frameAviso.place_forget()
        Button.buttonfechar.place_forget()

Interface.principal.mainloop()