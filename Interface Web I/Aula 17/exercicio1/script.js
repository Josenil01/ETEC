const titulo = document.querySelector('#titulo')
const nome = document.getElementById('nome')
const cp = document.getElementById('cp')
const botao = document.querySelector('#btn-sortear')
const tipoTag = document.querySelector('#tipo')
const card = document.getElementById('card')

// const pokemon = ['Pikachu', 'Bulbasaur', 'Charmander', 'Squirtle']
// const tipo = ['Eletrico', 'Planta', 'Fogo', 'Agua']


const pokeMurilo = [
    {nome:'Pikachu', tipo:"Eletrico", color : '#f1c40f'},
    {nome:'Bulbasaur', tipo:"Planta", color :'#2ecc71' },
    {nome:'Charmander', tipo:"Fogo",color :'#e74c3c'},
    {nome:'Squirtle', tipo:"Agua",color:'#3498db' },  
]

botao.addEventListener('click',
    function(){
         indiceSorteado = Math.floor(Math.random() * pokeMurilo.length)
         pokemonSorteado = pokeMurilo[indiceSorteado]

        cpSorteado = Math.floor(Math.random() * 2500) + 500
        // tipoSorteado = tipo[indiceSorteado]
        console.log(nome, cp)
        titulo.textContent = pokemonSorteado.nome
        tipoTag.textContent = pokemonSorteado.tipo  //tipoSorteado;

        nome.textContent = pokemonSorteado.nome
        cp.textContent = cpSorteado

        card.style.backgroundColor = pokemonSorteado.color
        card.style.display = 'block'
        
    }
)