def saudacoesGUI(nome):
    import random
    frases = ["Bom dia , meu nome é" +nome+"Como vai você hoje?" , "tudo bem?"]
    print(frases[random.randint(0,2)])

def salvasugestao(sugestao):
    with open ("baseconhecimento.txt", "a+") as conhecimento:
        conhecimento.write("Chatbot:",+ sugestao+"\n")    

def buscaRespostaGUI(texto):
    with open("baseConhecimento.txt", "a+") as conhecimento:
        conhecimento.seek(0)
        while True:
            viu = conhecimento.readline()
            if viu != "":
               if jaccard(texto,viu) > 0.3:
                   proximaLinha = conhecimento.readline()
                   if "Chatbot:" in proximaLinha:
                       return proximaLinha
            else:
                       conhecimento.write('\n' + texto)
                       return"me desculpe,nao sei oque falar"
def jaccard(textoUsuario,textobase):
    textoUsuario = limpaFrase(textoUsuario)
    textobase = limpaFrase(textobase)
    if len(textobase)< 1: return 0
    else:
        palavrasEmComum=0
        for palavra in textoUsuario.split():
            if palavra in textobase.split():
                palavrasEmComum =+1
                return palavrasEmComum/(len(textobase.split()))
            
def limpaFrase(Frase):
    tirar = ["?","!","...",".",",",":","Cliente:","\n"]
    for t in tirar:
        Frase = Frase.replace(t,"")
    Frase = Frase.upper()
    return Frase
            
def exibeRespostaGUI(texto,resposta,nome):
    return resposta.replace("ChatBot",nome)
                           

    


        
        
        
    