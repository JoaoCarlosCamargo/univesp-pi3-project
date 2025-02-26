// Fun��o para ler o texto
function lerTexto(texto) {
//    console.log("Fun��o lerTexto foi chamada");  // Log de depura��o
    const speech = new SpeechSynthesisUtterance(texto);
    speech.lang = 'pt-BR';  // Define o idioma como portugu�s do Brasil
    speech.rate = 1;        // Velocidade da fala (1 � o valor padr�o)
    speech.pitch = 1;       // Tom da fala (1 � o valor padr�o)

    // Inicia a s�ntese de voz
//    console.log("Iniciando a leitura do texto: ", texto);  // Log de depura��o com o texto a ser lido
    window.speechSynthesis.speak(speech);
}

// Adiciona evento ao bot�o para ler o texto
document.getElementById('ler-texto-btn').addEventListener('click', function() {
//    console.log("Bot�o foi clicado");  // Log de depura��o

    // Recupera o texto a ser lido
    const conteudo = document.getElementById('conteudo').innerText;
    const texto = document.getElementById('texto-a-ler').innerText;

//    console.log("Texto recuperado: ", conteudo, texto);  // Log de depura��o do texto

    // Junta o conte�do e o texto em uma string
    const textoCompleto = conteudo + ". " + texto;

    // Chama a fun��o para ler o texto
    lerTexto(textoCompleto);
});

// Adiciona evento ao bot�o para ler o texto
document.getElementById('ler-texto-btn2').addEventListener('click', function() {
//    console.log("Bot�o foi clicado");  // Log de depura��o

    // Recupera o texto a ser lido
    const conteudo = document.getElementById('conteudo2').innerText;
    const texto = document.getElementById('texto-a-ler2').innerText;

//    console.log("Texto recuperado: ", conteudo, texto);  // Log de depura��o do texto

    // Junta o conte�do e o texto em uma string
    const textoCompleto = conteudo + ". " + texto;

    // Chama a fun��o para ler o texto
    lerTexto(textoCompleto);
});

// Adiciona evento ao bot�o para ler o texto
document.getElementById('ler-texto-btn3').addEventListener('click', function() {
//    console.log("Bot�o foi clicado");  // Log de depura��o

    // Recupera o texto a ser lido
    const conteudo = document.getElementById('conteudo3').innerText;
    const texto = document.getElementById('texto-a-ler3').innerText;

//    console.log("Texto recuperado: ", conteudo, texto);  // Log de depura��o do texto

    // Junta o conte�do e o texto em uma string
    const textoCompleto = conteudo + ". " + texto;

    // Chama a fun��o para ler o texto
    lerTexto(textoCompleto);
});