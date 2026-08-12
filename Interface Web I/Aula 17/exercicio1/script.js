const titulo = document.querySelector('#titulo');
const botao = document.querySelector('#btn-sortear');
const tipoTag = document.querySelector('#tipo');

const pokemon = ['Pikachu', 'Bulbasaur', 'Charmander', 'Squirtle']
const tipo = ['Eletrico', 'Planta', 'Fogo', 'Agua']

botao.addEventListener('click',
    function(){
        indiceSorteado = Math.floor(Math.random() * pokemon.length)
        pokemonSorteado = pokemon[indiceSorteado]
        tipoSorteado = tipo[indiceSorteado]

        titulo.textContent = pokemonSorteado;
        tipoTag.textContent = tipoSorteado;
        
    }
)