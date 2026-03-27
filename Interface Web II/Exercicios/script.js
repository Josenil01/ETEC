const pokedexPreview = document.getElementById('live-pokedex-preview');
const cintoPreview = document.getElementById('live-cinto-preview');
const arenaPreview = document.getElementById('live-arena-preview');
const btnFugir = document.getElementById('btn-fugir');

// --- 1. Laço forEach (Listas Complexas) ---
const pokemonData = [
  { nome: 'Bulbasaur', tipo: 'Planta / Veneno', img: '1', cor: 'bg-green-100 border-green-300' },
  { nome: 'Charmander', tipo: 'Fogo', img: '4', cor: 'bg-red-100 border-red-300' },
  { nome: 'Squirtle', tipo: 'Agua', img: '7', cor: 'bg-blue-100 border-blue-300' },
];

pokemonData.forEach((pkmn) => {
  const card = document.createElement('div');
  card.className = `flex cursor-pointer flex-col items-center rounded-xl border p-4 shadow-sm transition-transform hover:-translate-y-1 ${pkmn.cor}`;
  card.innerHTML = `
    <img src="https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/${pkmn.img}.png" alt="${pkmn.nome}" class="h-24 w-24 drop-shadow-md">
    <h3 class="mt-2 text-lg font-bold text-slate-800">${pkmn.nome}</h3>
    <span class="text-xs font-bold uppercase tracking-wider text-slate-600 opacity-80">${pkmn.tipo}</span>
  `;
  pokedexPreview.appendChild(card);
});

// --- 2. Laço for (Repetições Exatas) ---
for (let i = 1; i <= 6; i++) {
  const pokebola = document.createElement('div');
  pokebola.className = 'relative flex h-12 w-12 cursor-pointer items-center justify-center overflow-hidden rounded-full border-4 border-white bg-red-500 shadow-md transition-transform hover:rotate-12';
  pokebola.innerHTML = `
    <div class="absolute bottom-0 h-1/2 w-full bg-white"></div>
    <div class="absolute h-1 w-full bg-slate-800"></div>
    <div class="z-10 h-4 w-4 rounded-full border-2 border-slate-800 bg-white"></div>
  `;
  cintoPreview.appendChild(pokebola);
}

// --- 3. Laço while (Condição de Limpeza) ---
btnFugir.addEventListener('click', () => {
  while (arenaPreview.firstChild) {
    arenaPreview.removeChild(arenaPreview.firstChild);
  }

  arenaPreview.innerHTML = '<span class="font-bold italic text-slate-500">A arena esta limpa.</span>';
  btnFugir.textContent = 'Voce escapou em seguranca!';
  btnFugir.classList.replace('bg-rose-500', 'bg-slate-400');
  btnFugir.classList.replace('hover:bg-rose-600', 'hover:bg-slate-500');
  btnFugir.disabled = true;
});