
const form = document.querySelector('#form-pokemon')
const feedback = document.querySelector('#feedback')
const listaCards = document.querySelector('#lista-cards') // não existe

console.log('script')

const URL_POKEAPI = 'https://pokeapi.co/api/v2/pokemon'

async function buscarDadosPokemon(nome)
{

    
    const nomeFormatado = nome.toLowerCase().trim()

    try{
        const resposta  = await fetch(`${URL_POKEAPI}/${nomeFormatado}`)

        if(!resposta.ok)
        {
            throw new Error('Pokemon não encontrado na PokeAPI')
        }

        const dados = await resposta.json();
        return dados
    }
    catch(error){
        console.log(" Não foi possivel carregar os dados do pokemon solicitado na PokeAPI",error)
        return [];
    }

}

function extrairImagemPokemon(dadosPokemon)
{
    if(!dadosPokemon)
    {
        console.log("Dados Vazios")
        return null
    }

    // console.log(dadosPokemon.sprites)
    // console.log(artWorkOfficial) 
    //  console.log(spriteDefault)
    const artWorkOfficial = dadosPokemon.sprites?.other?.['official-artwork']?.front_default
    const spriteDefault = dadosPokemon.sprites?.front_default   
    return artWorkOfficial || spriteDefault || null
}

function extrairTipoPokemon(dadosPokemon)
{
    if(!dadosPokemon || !dadosPokemon.types)
    {   
        console.log("Dados vazios")
        return null
    }
    // console.log(dadosPokemon.types)
    
    //Tratamento para lidar com arrays
    const  tipos = dadosPokemon.types.map(function(item){
        // console.log( item.type.name)
        return item.type.name 
    })
    return tipos
}

function extrairCombatPower(dadosPokemon)
{
    if(!dadosPokemon || !dadosPokemon.base_experience)
    {   
        console.log("Dados vazios")
        return null
    }
    return xp = dadosPokemon.base_experience
}

// nome,imagem, tipo, xp , treinador = "none"
function criarCardPokemon(nome, imagem, tipo, combatPower)
{
    const card = document.createElement('div')
    card.className = 'card-pokemon'

    const img = document.createElement('img')
    img.className = 'card-pokemon-img'
    img.src = imagem || 'https://placehold.co/96x96?text=?'
    img.alt = nome

    const nomeCard = document.createElement('h3')
    nomeCard.className  = 'card-pokemon-nome'
    nomeCard.textContent = nome

    const  infoTipo  = document.createElement('p')
    infoTipo.className = 'card-pokemon-info'
    infoTipo.textContent = `Tipo:${tipo || 'desconhecido'}`

    const cp = document.createElement('p')
    cp.className = 'card-pokemon-info'
    cp.textContent =   `CP: ${combatPower|| '000'}`

    card.append(img,nomeCard,infoTipo,cp)

    listaCards.appendChild(card)

    console.log(card, img, nomeCard)
}




form.addEventListener('submit',
   async function(event)
    {
        event.preventDefault(); //impedindo de recarregar a pagina
        const nome = document.querySelector('#nome').value.trim();
        const tipo = document.querySelector('#tipo').value.trim();
        const cp = Number(document.querySelector('#cp').value.trim());
        const treinador = document.querySelector('#treinador').value.trim();

        if(nome.length < 3)
        {
            console.log("O campo precisa ter mais de 3 caracteres.")
            
            feedback.textContent = "❌ Nome deve conter ao menos 3 caracteres."
            feedback.style.color = 'red'
            return;
        }

        else if(cp <100)
        {
            feedback.textContent = "❌ O poder do pokemon precisa ser maior que 100."
            feedback.style.color = 'red'
            return;
        }
        else{
            feedback.textContent = "✅ Pokemon cadastrado com sucesso."
            feedback.style.color = 'green'
        }
       

        
    }
)
function limparCampos()
{
    document.querySelector('#nome').value = '';
    document.querySelector('#tipo').value = '';
    document.querySelector('#cp').value = '';
    document.querySelector('#treinador').value = '';
}

const nome = document.querySelector('#nome')
// ela tambem deve criar o autocomplete
nome.addEventListener('input',
    function()
    {
        if(nome.value.trim().length < 3){

            feedback.textContent = "❌ Nome deve conter ao menos 3 caracteres."
            feedback.style.color = 'red'
        }
        else{

              feedback.textContent = ""
        
        debounceBusca = setTimeout(
        async function()
        {
            console.log(nome.value);
        const dadosApi =  await buscarDadosPokemon(nome.value)
        const nomePokemon = dadosApi.name //
        const imagemURL = extrairImagemPokemon(dadosApi)
        const tipoPokemon = extrairTipoPokemon(dadosApi)
        const combatPower = extrairCombatPower(dadosApi)
        
        //para visualizar apenas
        criarCardPokemon(nomePokemon,imagemURL, tipoPokemon) //
        
        const tipo = document.querySelector('#tipo')
        const cp =document.querySelector('#cp')
        console.log(tipoPokemon)
        tipo.value = tipoPokemon
        cp.value = combatPower
       


        console.log("passou");
    }, 1000)
}
    }
);

