const btnPortal = document.getElementById('btn-portal');
const loader = document.getElementById('loader');
const areaResultadoTop = document.getElementById('div-resultado-top');
const areaResultadoButton = document.getElementById('div-resultado-button');

let card1 = null;
let card2 = null;
let id = null;


areaResultadoTop.addEventListener('click', (event) => {
   
    const cardClicado = event.target.closest('.char-card');
   
    if (cardClicado) {
        cardClicado.classList.toggle('escondido');
        if(id === null)
        {
            id = cardClicado.dataset.key;
            card1 = cardClicado;
            console.log(id);
        }
        else{
            if(id === cardClicado.dataset.key)
            {
               card1.classList.add('certo');
               cardClicado.classList.add('certo');
               console.log(cardClicado.dataset.key);
               id = null;

            }
            else
            {
                console.log('Cards não combinam', card1.dataset.key, cardClicado.dataset.key);
                id = null;
                setTimeout(() => {
                    card1.classList.add('escondido');
                    cardClicado.classList.add('escondido');
                }, 1000);
            }
        }   
    }
});


btnPortal.addEventListener('click', async () => {
    areaResultadoTop.innerHTML = '';
    areaResultadoButton.innerHTML = '';
    loader.classList.remove('hidden');
    areaResultadoTop.classList.add('resultado-api');
    areaResultadoButton.classList.add('resultado-api');

    try {
        const personagens = await carregarPersonagens();       
        const personagensEmbaralhados = [...personagens, ...personagens].sort(() => Math.random() - 0.5);
       
        let htmlCardsTop = '';
          personagensEmbaralhados.forEach(personagem => {
            console.log('Personagem:', personagem);
            htmlCardsTop += `
            <div class="char-card escondido" data-key="${personagem.id}">
                <img src="${personagem.image}" alt="${personagem.name}">
                <div class="char-info">
                    <h3>${personagem.name}</h3>
                    <p>Status: ${personagem.status}</p>
                    <p>Espécie: ${personagem.species}</p>
                </div>
            </div>
            `;
        });



        areaResultadoTop.innerHTML = htmlCardsTop;
        // areaResultadoButton.innerHTML = htmlCardsButton;

    } catch (error) {
        console.error('Erro ao buscar personagem:', error);
        areaResultadoTop.innerHTML = '<p>Erro ao carregar os personagens.</p>';
        // areaResultadoButton.innerHTML = '<p>Erro ao carregar os personagens.</p>';
    } finally {
        loader.classList.add('hidden');
    }
});


async function carregarPersonagens() {
    const data = [];

    for (let i = 1; i <= 4; i++) {
        const idAleatorio = Math.floor(Math.random() * 826) + 1;
        const resposta = await fetch(`https://rickandmortyapi.com/api/character/${idAleatorio}`);
        const personagemJson = await resposta.json();
        data.push(personagemJson);
    }

    return data;
}