const pokeContainer = document.querySelector("#poke-container"); // Change this to select the container element instead of the #poke element

function getRandomPokemon() {
    const randomId = Math.floor(Math.random() * 898) + 1;
    return fetch(`https://pokeapi.co/api/v2/pokemon/${randomId}`)
        .then(response => response.json());
}

function mostrarPokemon(poke) {
    let tipos = poke.types.map((type) => `<p class="${type.type.name} tipo">${type.type.name}</p>`);
    tipos = tipos.join('');

    const div = document.createElement("div");
    div.classList.add("pokemon");
    div.innerHTML = `
    <div class="pokemon">
        <h1 class="pokemon-nombre">${poke.name}</h1>
        <img class="pokemon-image" src="${poke.sprites.other["official-artwork"].front_default}" alt="Pokemon Image">
        <p class="pokemon-id-back">${poke.id}</p>
        <div class="pokemon-tipos">
                    ${tipos}
                </div>
        <div class="overlay">
        <h3>Pokemon del Dia</h3>
        <p>Muestra un Pokemon al azar cada que se recarga la página</p>
        </div>
    </div>
`;

    // Append the new pokemon div to the container
    pokeContainer.innerHTML = "";
    pokeContainer.appendChild(div);
}

// Call the function to get a random pokemon and display it
getRandomPokemon().then(mostrarPokemon);