const lista = [
    "El Padrino",
    "Titanic",
    "El Señor de los Anillos: La Comunidad del Anillo",
    "Forrest Gump",
    "Pulp Fiction",
    "Matrix",
    "La Lista de Schindler",
    "El Rey León",
    "El Resplandor",
    "Volver al Futuro",
    "Jurassic Park",
    "Gladiator",
    "Interestelar",
    "La La Land",
    "El Gran Dictador",
    "El Club de la Lucha",
    "El Laberinto del Fauno",
    "La Vida es Bella",
    "Interestelar",
    "Parásitos"
  ];
  console.log('---- Array de peliculas----')
  const arrayMap = lista.map((peli) => `<li>${peli}</li>`)
  console.log(arrayMap)
  console.log('----Con Join----')
  const mapeo = `<ul>${lista.map((peli) =>  `<li>${peli}</li>`).join("")}</ul>`;
  console.log(mapeo)
  console.log('---- Sin Join----')
  const mapeoDos = `<ul>${lista.map((peli) =>  `<li>${peli}</li>`)}</ul>`;
  console.log(mapeoDos)
  document.getElementById('root').innerHTML = `<ul>${lista
    .map((peli) =>  `<li>${peli}</li>`)
    .join('')}</ul>`;
  