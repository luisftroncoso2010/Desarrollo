const listadoNoticias = [{
    titulo: "La emocion de Lisandro Martínez",
    epigrafe: "La increíble ovación de los hinchas de Manchester United al defensor argentino: 'Quise llorar'",
    foto:"./img/futbol.webp"
    },
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


// Insertar datos de manera dinamica. (alt = img)
const imagenes = document.querySelectorAll(".noticias article img");
console.log(imagenes);

// Se le agrega el "alt" con su respectivo atributo
imagenes[0].setAttribute("alt", "miniatura de noticias");

/* Capturamos el main (Para agregar los otros elementos, atravesd del array) */
const main = document.querySelector(".noticias");

// Hay que limpiar la etiqueta antigua. Si no se repetira alguna etiqueta
main.innerHTML = "";

// Iteramos el listado de noticias para cargar lo nuevo
listadoNoticias.forEach(noticias => {
    // Creamoa objetos/Etiquetas nuevos que no existen en el DOM
    const article = document.createElement("article");
    const h2 = document.createElement("h2");
    const img = document.createElement("img");
    const p = document.createElement("p");


    /* 
    Agregamos los titulos, textos y atributos de cada etiqueta creada
    */
    h2.innerText = noticias.titulo;
    img.setAttribute("src", noticias.foto);
    img.setAttribute("alt", noticias.titulo);
    p.textContent = noticias.epigrafe;
    

    /*
     Tecnica de insercion de nodos. 
     Agregamos cada elemento a la etiqueta padre (articles)
    */
    article.appendChild(h2);
    article.appendChild(img);
    article.appendChild(p);


    // Agrego el article creado al elemento padre (main (Tiene clase noticias))
    main.appendChild(article);
});


// Tecnica de inyeccion de template iterals temple iterals
/* main.innerHTML += '

';*/