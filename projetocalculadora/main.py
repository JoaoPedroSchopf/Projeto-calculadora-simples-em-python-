from tkinter import * 
from tkinter import ttk 

#cores

cor1= "#1A1A1A" #preta
cor2= "#feffff" #braco
cor3= "#38576b" #azul 
cor4= "#949494" #cinza
cor5= "#FFAB40" #laranja


janela = Tk()
janela.title("Calculadora")
janela.geometry("235x309")#tamanho da janela
janela.config(bg=cor1)

#permitir expansão de frame(cores em tela cheia do mesmo modo)
janela.rowconfigure(0, weight=1)
janela.rowconfigure(1, weight=5)
janela.columnconfigure(0, weight=1)

#frames
frame_tela = Frame(janela, width=235, height=50, bg=cor3)
frame_tela.grid(row=0, column=0, sticky="nsew")

frame_corpo = Frame(janela, width=235, height=268)
frame_corpo.grid(row=1, column=0, sticky="nsew")


#variavel todos valores 
todos_valores= ''

valor_texto=StringVar()


#parte logica de calculo
#criando função
def entrar_valores(valor):
    global todos_valores

    todos_valores=todos_valores+str(valor)

    #passando valor para a tela
    valor_texto.set(todos_valores)


#função p/calcular valores 
def calcular():
    global todos_valores
    resultado=eval(todos_valores)
    valor_texto.set(str(resultado))
    todos_valores = str(resultado)


#função limpar tela
def limpar_tela():
    global todos_valores
    todos_valores=""
    valor_texto.set("")    


#label 

app_label= Label(frame_tela, textvariable=valor_texto, width=16, height=2, padx=7, relief=FLAT, anchor="e", justify=RIGHT, font=('Ivy 18 '), bg=cor3, fg= cor2)
app_label.place(x=0, y=0)


#botões PRIMEIRA FILEIRA
b_1= Button(frame_corpo, text="C",command= limpar_tela,  width=11, height=2, bg=cor4, font=("Ivy 13 bold"), relief=RAISED, overrelief=RIDGE)
b_1.place(x=0,y=0)#localização do botão 'c'

b_2= Button(frame_corpo, command= lambda:entrar_valores('%'),text="%", width=5, height=2, bg=cor4, font=("Ivy 13 bold"), relief=RAISED, overrelief=RIDGE)
b_2.place(x=118,y=0)#localização do botão '%'

b_3= Button(frame_corpo,command= lambda:entrar_valores('/'), text="/", width=5, height=2, bg=cor5, fg=cor2, font=("Ivy 13 bold"), relief=RAISED, overrelief=RIDGE)
b_3.place(x=176,y=0)#localização do botão '/'


#botões SEGUNDA FILEIRA
b_4= Button(frame_corpo,command= lambda:entrar_valores('7'), text="7", width=5, height=2, bg=cor4, font=("Ivy 13 bold"), relief=RAISED, overrelief=RIDGE)
b_4.place(x=0,y=52)#localização do botão '7'
b_5= Button(frame_corpo,command= lambda:entrar_valores('8'), text="8", width=5, height=2, bg=cor4, font=("Ivy 13 bold"), relief=RAISED, overrelief=RIDGE)
b_5.place(x=59,y=52)#localização do botão '8'
b_6= Button(frame_corpo,command= lambda:entrar_valores('9'), text="9", width=5, height=2, bg=cor4, font=("Ivy 13 bold"), relief=RAISED, overrelief=RIDGE)
b_6.place(x=118,y=52)#localização do botão '9'
b_7= Button(frame_corpo,command= lambda:entrar_valores('*'), text="*", width=5, height=2, bg=cor5, fg=cor2, font=("Ivy 13 bold"), relief=RAISED, overrelief=RIDGE)
b_7.place(x=176,y=52)#localização do botão '*'

#botões TERCEIRA FILEIRA
b_8= Button(frame_corpo,command= lambda:entrar_valores('4'), text="4", width=5, height=2, bg=cor4, font=("Ivy 13 bold"), relief=RAISED, overrelief=RIDGE)
b_8.place(x=0,y=104)#localização do botão '4'
b_9= Button(frame_corpo,command= lambda:entrar_valores('5'), text="5", width=5, height=2, bg=cor4, font=("Ivy 13 bold"), relief=RAISED, overrelief=RIDGE)
b_9.place(x=59,y=104)#localização do botão '5'
b_10= Button(frame_corpo,command= lambda:entrar_valores('6'), text="6", width=5, height=2, bg=cor4, font=("Ivy 13 bold"), relief=RAISED, overrelief=RIDGE)
b_10.place(x=118,y=104)#localização do botão '6'
b_11= Button(frame_corpo,command= lambda:entrar_valores('-'), text="-", width=5, height=2, bg=cor5, fg=cor2, font=("Ivy 13 bold"), relief=RAISED, overrelief=RIDGE)
b_11.place(x=176,y=104)#localização do botão '-'


#botões QUARTA FILEIRA

b_12= Button(frame_corpo,command= lambda:entrar_valores('1'), text="1", width=5, height=2, bg=cor4, font=("Ivy 13 bold"), relief=RAISED, overrelief=RIDGE)
b_12.place(x=0,y=156)#localização do botão '7'


b_13= Button(frame_corpo,command= lambda:entrar_valores('2'), text="2", width=5, height=2, bg=cor4, font=("Ivy 13 bold"), relief=RAISED, overrelief=RIDGE)
b_13.place(x=59,y=156)#localização do botão '2'


b_14= Button(frame_corpo,command= lambda:entrar_valores('3'), text="3", width=5, height=2, bg=cor4, font=("Ivy 13 bold"), relief=RAISED, overrelief=RIDGE)
b_14.place(x=118,y=156)#localização do botão '3'


b_15= Button(frame_corpo,command= lambda:entrar_valores('+'), text="+", width=5, height=2, bg=cor5, fg=cor2, font=("Ivy 13 bold"), relief=RAISED, overrelief=RIDGE)
b_15.place(x=176,y=156)#localização do botão '+'

#QUINTA fileira igual a primeira
b_16= Button(frame_corpo,command= lambda:entrar_valores('0'), text="0", width=11, height=2, bg=cor4, font=("Ivy 13 bold"), relief=RAISED, overrelief=RIDGE)
b_16.place(x=0,y=208)#localização do botão '0'

b_17= Button(frame_corpo,command= lambda:entrar_valores('.'), text=".", width=5, height=2, bg=cor4, font=("Ivy 13 bold"), relief=RAISED, overrelief=RIDGE)
b_17.place(x=118,y=208)#localização do botão '.'

b_18= Button(frame_corpo,command=calcular , text="=", width=5, height=2, bg=cor5, fg=cor2, font=("Ivy 13 bold"), relief=RAISED, overrelief=RIDGE)
b_18.place(x=176,y=208)#localização do botão '='








janela.mainloop()