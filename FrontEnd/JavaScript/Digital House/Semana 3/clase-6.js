function marcarFavoritos(albumes){
    // Seleccionar todos los botones
    const botonesDeLike = document.querySelectorAll(".fa-heart");
    
    botonesDeLike.forEach(boton => {
        boton.addEventListener("click", function(evento){
            console.log(evento)
            console.log(`Target Favoritios: ${evento.target}`)
            console.log(evento.target.class)
            
            // Capturamos el id de un album, para saber su estado
            let albumID = evento.target.id

            albumes.forEach(album => {
                // Comparamos el estado de 
                if(album.id == albumID){
                    console.log(`Coincide ${albumID} con ${album.id}`)
                    console.log(`La propiedad like es: ${album.like}`)
                    // cambiamos de true a false. LA negamos
                    album.like = !album.like
                    console.log(`La propiedad like ahora es: ${album.like}`)
                }
            })
            // renderizarAlbunes(albumesFamosos)
            // Actualizamos toda la info, es decir colcoamos todas las terjetas y se muestren
            renderizarAlbunes(albumesFamosos)             
            contarFavoritos(albumesFamosos)
            // Hacemos la llamada recursiva para validar volver a usar
            marcarFavoritos(albumesFamosos)
        })       
    })
}
marcarFavoritos();

/*                         FUNCION: Eliminar album                        */
/* -------------------------------------------------------------------------- */
// Debemos desarrollar la funcion de eliminar un album. Para esto le vamos a 
// preguntar al usuario cual quiere eliminar.
// Vamos a seguir las indicaciones que nos permiten lograrlo utilizando eventos.
// 1- Hay que escuchar el evento de 'keydown' para detectar cuando el usuario
// presiona la tecla f✅
// 2- Una vez que detectamos la tecla, debemos mostrarle un prompt al usuario
// para que ingrese el nombre del album que desea eliminar
// 3- Podemos buscar la posicion del almbum buscado en el array con la funcion .findIndex()
// 4- Si la busqueda nos da un resultado válido, procedemos a borrar el objeto del array
// 5- Acto seguido debemos llamar a las funciones de renderizar y marcar favorito para que sean nuevamente aplicadas.

window.addEventListener("keydown", eliminarAlbum)
function eliminarAlbum(evento){
    //console.log(evento)    
    //console.log(evento.code)

    if(evento.code == "KeyF"){
        console.log("Has precionado la letra f")
        const albumAEliminar = prompt("¿Que album quieres eliminar?").toLowerCase()
        console.log(`Posicion eliminar: ${albumAEliminar}`)

        const nombre = albumesFamosos.findIndex(album => album.nombre.toLowerCase() === albumAEliminar)
        console.log(nombre) 

        if(nombre == -1) {
            alert("Este album no existe")
        }else {
            albumesFamosos.splice(nombre, 1)
        }
        renderizarAlbunes(albumesFamosos)             
        contarFavoritos(albumesFamosos)
        // Hacemos la llamada recursiva para validar volver a usar
        marcarFavoritos(albumesFamosos)       
    }       
}



   

