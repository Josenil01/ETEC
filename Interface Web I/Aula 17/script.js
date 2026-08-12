const titulo = document.querySelector('#titulo');
const saida = document.querySelector('#saida');
const botao = document.querySelector('#btn');

// trocar o texto do botão para Hora Atual


botao.addEventListener('click',
    function(){
        saida.textContent = 'Clicou às ' + new Date().toLocaleTimeString();
        titulo.style.color = 'blue';
    }
)

