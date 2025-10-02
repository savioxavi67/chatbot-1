// faca um codigo que tenha um codigo de texto(input) e um botao(button)
//  o botao ao ser clicado ira adicionar em uma lista o texto
//escrito no campo de texto

let items = [];

function adicionar(){
    let texto = document.getElementById("entrada").value;

    if(texto != ""){
        items.push(texto);
        document.getElementById("entrada").value = "";

        mostrarLista();
    }
}

function mostrarLista(){
    let lista = document.getElementById("lista")

    for(let contagem = 0; contagem < items.length; contagem++){
        let li = document.createElement("li");
        
        li.textContent = items[contagem];
        lista.appendChild(li);

    }
}

function remover(){
    if(items.length > 0);
    items.pop();
    mostrarLista();
}