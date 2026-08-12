const btnPortal = document.getElementById('btn-portal');
const loader = document.getElementById('loader');
const areaResultadoTop = document.getElementById('div-resultado-top');
const areaResultadoButton = document.getElementById('div-resultado-button');


btnPortal.addEventListener('click', async () => {
    areaResultadoTop.innerHTML = '';
    loader.classList.remove('hidden');
    areaResultadoTop.classList.add('resultado-api');
  

    try {
        const dados = [];

        for (let i = 0; i < 4; i++) 
        {
            const idAleatorio = Math.floor(Math.random() * 826) + 1; // Gera um ID aleatório entre 1 e 826
            const personagens = await fetch(`https://rickandmortyapi.com/api/character/${idAleatorio}`);
            const personagemJson = await personagens.json();
            dados.push(personagemJson);
        }
    console.log('Dados recebidos da API:', dados);
    
       //dados [p1,p2,p3,p4]
        let htmlCardsTop = '';
        //personagensEmbaralhados [p1,p2,p3,p4 , p3,p4,p1,p2]
          const personagensEmbaralhados = [...dados,...dados.sort(() => Math.random() - 0.5)];
        personagensEmbaralhados.forEach(personagemJson => {
            htmlCardsTop += `
            <div class="char-card escondido" data-key="${personagemJson.id}">
                <img src="${personagemJson.image}" alt="${personagemJson.name}">
                <div class="char-info">
                    <h3>${personagemJson.name}</h3>
                    <p>Status: ${personagemJson.status}</p>
                    <p>Espécie: ${personagemJson.species}</p>
                </div>
            </div>
            `;
        });
           
        areaResultadoTop.innerHTML = htmlCardsTop;
        // Embaralha os personagens para o botão
        
        // areaResultadoButton.classList.add('resultado-api');
        // let htmlCardsButton = '';
        // personagensEmbaralhados.forEach(personagemJson => {
        //     htmlCardsButton += `
        //     <div class="char-card " data-key="${personagemJson.id}">
        //         <img src="${personagemJson.image}" alt="${personagemJson.name}">
        //         <div class="char-info">
        //             <h3>${personagemJson.name}</h3>
        //             <p>Status: ${personagemJson.status}</p>
        //             <p>Espécie: ${personagemJson.species}</p>
        //             <p>Gênero: ${personagemJson.gender}</p>
        //         </div>
        //     </div>
        //     `;
        // });
        
        // areaResultadoButton.innerHTML = htmlCardsButton;
    } catch (error) {
        console.error('Erro ao buscar personagem:', error);
        areaResultadoTop.innerHTML = '<p>Erro ao carregar os personagens.</p>';
     
    } finally {
        loader.classList.add('hidden');
    }
});
