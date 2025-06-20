const cabecalho_subtitulo = document.querySelector(".cabecalho_subtitulo");
cabecalho_subtitulo.textContent = ''; 

function efeito_digitação(texto, contador){
    if(contador < texto.length) {
        setTimeout(() => {
            cabecalho_subtitulo.textContent += texto.charAt(contador);
            contador++;
            efeito_digitação(texto, contador); 
        }, 120);
    }
}

efeito_digitação("Seja muito bem vindo(a)!", 0);
