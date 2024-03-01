const listadoNoticias = [
    {
    titulo: "La renuncia de Liz Truss",
    epigrafe: "Boris Johnson interrumpío sus vacaciones y vulve a sonar fuerte entre los posibles suscesores.",
    foto:"./img/boris.webp"
    },
    {
    titulo: "Los motivos",
    epigrafe: "Una escuela de argentina fue elegida entre las diez mejores del mundo.",
    foto: "./img/escuela.webp"
    }    
];



/* Capturamos el main */
const main = document.querySelector(".noticias"); 
// Recorremos el listado de noticias para cargarlas dinámicamente
listadoNoticias.forEach(noticia => {
    main.innerHTML += `
      <article>
          <h2>${noticia.titulo}</h2>
          <img src="${noticia.foto}" alt="${noticia.titulo}">
          <p>${noticia.epigrafe}.</p>
      </article>`;
  });



