def saudacoes(nome):
    import random
    frases = ["Bom dia , meu nome é" +nome+"Como vai você hoje?" , "tudo bem?"]
    print(frases[random.randint(0,2)])

def recebetexto():
    texto = "Cliente: "+input("Cliente: ")
    palavrasProibidas = ["idiota", "paspalho", "bocó"]
    for p in palavrasProibidas:
        if p in texto:
            print("olha a boquinha")
            return recebetexto()
    return texto
def buscaResposta(nome, texto):
    with open("baseConhecimento.txt", "a+") as conhecimento:
        conhecimento.seek(0)
        while True:
            viu = conhecimento.readline()
            if viu != "":
                if  texto.replace("Cliente:","")=="tchau":
                    print(nome+"; volte sempre")
                    return "fim"
                elif viu.strip() == texto.strip():
                    proximalinha= conhecimento.readline()
                    if "chatbot:" in proximalinha:
                        return proximalinha 
            else:
                print("Não sei responder a pergunta")
                conhecimento.write("\n" + texto)
                respostaEsperado = input("Oque esperava? \n")
                conhecimento.write("\n" + "chatbot:"+ respostaEsperado)
                return "obrigado" 
            
def exibeResposta(resposta,nome):
    print(resposta.replace("chatbot", nome))
    if resposta == "fim":
        return "fim"
    return "continua"           

                           

    


        
        
        
    