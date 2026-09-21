const feedback = document.getElementById('feedback')
const URL_API= 'https://jsonplaceholder.typicode.com/users'

async function entrar(event) {
    event.preventDefault()
    feedback.textContent="Verificando sua identidade!"

    try{
        const resposta = await fetch(`${URL_API}/1`)
        const dados  = await resposta.json()
        feedback.textContent = `Status: ${resposta.status} OK \n\n` + JSON.stringify(dados, null,2)
    }
    catch(error)
    {
        feedback.textContent = "Erro na requisição GET: " + error
    }

    
}


