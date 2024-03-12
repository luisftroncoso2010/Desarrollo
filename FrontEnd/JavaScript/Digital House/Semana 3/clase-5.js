/* --------------------------- listado de almbumes --------------------------- */
const albumesFamosos = [{
    id: "x123",
    nombre: "Nevermind",
    imagen: "https://m.media-amazon.com/images/I/71DQrKpImPL._SL1400_.jpg",
    like: false
},
{
    id: "y456",
    nombre: "Thriller",
    imagen: "https://img.discogs.com/LfnH5tbhcZ4xRMNLAodIyvea9xA=/fit-in/600x600/filters:strip_icc():format(webp):mode_rgb():quality(90)/discogs-images/R-294033-1151290881.jpeg.jpg",
    like: true
},
{
    id: "z789",
    nombre: "The wall",
    imagen: "https://img.discogs.com/EbLYco6R1A-5Z7QJ4t4O1JSzsM8=/fit-in/587x600/filters:strip_icc():format(jpeg):mode_rgb():quality(90)/discogs-images/R-4620059-1370165707-3841.jpeg.jpg",
    like: true
},
{
    id: "a987",
    nombre: "Abbey Road",
    imagen: "https://cloudfront-us-east-1.images.arcpublishing.com/copesa/RDH5EPH2TNENPI73NBWUWWMLPA.jpg",
    like: false
},
{
    id: "b654",
    nombre: "Origin of Symmetry",
    imagen: "https://http2.mlstatic.com/D_NQ_NP_967206-MLA26105577132_102017-O.webp",
    like: true
},
{
    id: "c321",
    nombre: "Back in Black",
    imagen: "https://i1.wp.com/www.scienceofnoise.net/wp-content/uploads/2020/07/068660474366a63e1263e53ff370eb50.jpg",
    like: false
}];

// funcion captar nombre de usuario
function obtenerUsuario(){
    const nombreUsuario = document.querySelector('#nombreUsuario');
    let usuario = ""

    // Perdir nombre de uauario hasta que sea valido
    do{
        // Quitamos los espacios y lo converitmos a minisculas
        usuario = prompt("Ingrese su nombre de usuario: ").toLocaleLowerCase().trim();

    }while(usuario == null && usuario == "" && usuario.lenth < 3 );
    
    // Dividimos la cadena de Strings (split), por espacios y me crea un array
    let nombres = usuario.split(" ");    
    // Capturamos la primera letra de cada palabra y la convertimos en mayusculas, le agregamos el resto (slice) y unimos el array a un string (join)
    usuario = nombres.map(nombre => nombre.charAt(0).toUpperCase() + nombre.slice(1)).join(" ");
    
    // Insertar el dato en el html, atraves del selector
    nombreUsuario.textContent = usuario;

    // Agregamos atraves de documen usando el id y le pasamos el usuario
    //nombreUsuario.append(document.createTextNode(usuario));
    //nombreUsuario.innerText = usuario;

}
obtenerUsuario();


// Capturamos el selector 
function renderizarAlbunes(listado){

    // Capturamos el selector de las etiquetas html
    const covers = document.querySelector(".covers");
    //console.log(covers)
    covers.innerHTML  = "";

    listado.forEach(album => {
        /*
        const li = document.createElement("li");
        const img = document.createElement("img");
        const p = document.createElement("p");
        const i = document.createElement("i");
        
        // Agregamos los atributos de cada nodo de las etiquetas creadas
        li.setAttribute("data.id", album.id);

        img.setAttribute("src", album.imagen);
        img.setAttribute("alt", album.nombre);

        p.textContent = album.nombre;

        i.setAttribute("id", album.id);
        i.setAttribute("class", `fa fa-heart ${album.like ? "favorito" : ""}`);

        // Agregar los nuevos nodos al li
        li.appendChild(img);
        li.appendChild(p);
        li.appendChild(i);

        // Agregamos al la clase covers
        covers.appendChild(li);

        */
       // Metodo de insercion de templeta literals
       covers.innerHTML += `
       <li data-id="${album.id}">
            <img src="${album.imagen}" alt="${album.nombre}">
            <p>${album.nombre}</p>
            <i id="${album.id}" class="fa fa-heart ${album.like ? "favorito" : ""}"></i>
        </li>
       `
    });

    /*
    // Agregar event listener para cada corazón
    covers.querySelectorAll('.fa-heart').forEach(corazon => {
        corazon.addEventListener('click', function () {
            // Obtener el ID del álbum asociado al corazón
            const albumId = corazon.getAttribute('id');
            
            // Encontrar el álbum correspondiente en el array
            const album = listado.find(a => a.id === albumId);
            
            // Alternar la propiedad 'like' y la clase 'favorito'
            album.like = !album.like;
            corazon.classList.toggle('favorito');
        });
    });
    */


};
renderizarAlbunes(albumesFamosos);

/* -------------------------------------------------------------------------- */
/*                   [3] FUNCION: mostrar datos del usuario                   */
/* -------------------------------------------------------------------------- */
// Dentro del div '.perfil' tenemos un parrafo con 2 span en los que debemos colocar
// correctamente su contenido.
// Para eso debemos hacer ciertos calculos y colocar esa info en el HTML. Debemos:
// 1- contar la cantidad de albumes del array y pintarlo en el span correspondiente
// 2- contar la cantidad de favoritos y pintarlo en el span correspondiente
// 3- tener en cuenta: usar las palabra en plural o en singular, según cuando
// sea necesario ( es decir: 1 album, 1 favorito / 2 albumes, 3 favoritos )
function contarFavoritos(albumes) {
    const cantidadAlbumes = document.querySelector("#cant-albums"),
        cantidadFavortios = document.getElementById("cant-favoritos");
    
    let contadorAlbumes = 0,
        contadorFavoritos = 0;

    albumes.forEach(albumes => {
        contadorAlbumes++;
        if(albumes.like){
            contadorFavoritos ++;
        }

        if(contadorAlbumes == 1){
            cantidadAlbumes.textContent = `${contadorAlbumes} álbum`;
        }else{
            cantidadAlbumes.textContent = `${contadorAlbumes} álbumes`;
        }

        if(contadorFavoritos == 1){
            cantidadFavortios.textContent = `${contadorFavoritos} álbum`;
        }else{
            cantidadFavortios.textContent = `${contadorFavoritos} álbumes`;
        }        
    })
}
contarFavoritos(albumesFamosos);




