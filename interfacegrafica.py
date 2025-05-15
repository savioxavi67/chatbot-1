import chatbot as cb 
from tkinter import *


main_window = Tk()

main_window.title("chatbot")
main_window.geometry("500x700")
main_window.grid()

frame = Frame(main_window)
frame.grid()
labelIdentificacao = Label(frame,text = "insira uma mensagem aqui:")
labelIdentificacao.grid(row=0, column=0)

entradamensagem = Entry(frame)
entradamensagem.grid(row=0,column=1)

frame2 = Frame(main_window)
frame2.grid(row=1,column=0)
historico = StringVar()
Label(frame2,textvariable=historico).grid()

nomeMaquina = "chatinho"
historico.set("qual o seu nome:")

entradaSugestao = False
entradaSugestao = True
nomeUsuario = ""

def rodaChatbot():
    global entradaSugestao
    global entradaNomeUsuario
    global historicoConversas
    global nomeUsuario
    global nomeMaquina

    if entradaNomeUsuario:
        nomeUsuario = entradamensagem.get()
        saudacao = cb.saudacaoGUI(nomeMaquina)
        historicoConversa = nomeMaquina+ ":"+ saudacao + "\n"
        historico.set(historicoConversa)
        entradaNomeUsuario = False
    else:
        texto = entradamensagem.get()
        historicoConversa += "\n" + nomeUsuario + ":"+ texto
        historico.set(historicoConversa)

        if entradaSugestao:
            cb.salvasugestao(texto)
            entradaSugestao = False
            historicoConversa += "\n agora entendi,vamos continuar a conversa...\n"
            historicoConversa.set(historicoConversa)
        else:
            resposta = cb.buscaRespostaGUI("cliente:" +texto+"\n")
            if resposta == "me desculpe , nao sei oq falar":
                historicoConversa += "\n Me desculpe. oque voce esperava "
                entradaSugestao = False
            
            else:
                historicoConversa += "\n"+cb.exibeRespostaGUI(texto,resposta,nomeMaquina)
                historico.set(historicoConversa)

Button(frame,text="clique", command=rodaChatbot).grid(row=0,column=2)



main_window.mainloop()