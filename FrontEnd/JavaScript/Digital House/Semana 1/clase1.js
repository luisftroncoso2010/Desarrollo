function iniciarJuego(){
    // Saludar al visitante
    alert("Bienvenido al juego de piedra papel o tijeras de Frontend");

    // Pedir el nombre y guardar en una variable
    const nombre = prompt("Me puede indicar su nombre: ");
    alert("`Hola estimado desarrollador: " + nombre + ", mucha suerte");

    // MOstrando datos por consola 
    console.log(`---------------------`);
    console.log(`El nombre del jugador es: `)
    console.log(nombre);
    console.log(`----------------------`);


    return nombre;
}

let userName = iniciarJuego();
console.log(userName);


/* -------------------------------------------------------------------------- */
/*                          CONSIGNA                          */
/* -------------------------------------------------------------------------- */
// 1- Modificar la funcion de iniciarJuego(), validar si ingresa un dato válido como nombre.
// 2- Si no ingresa un texto, o tiene menos de 3 caracteres debemos volverle a pedir que lo ingrese.
// 3- Finalmente el nombre devuelto debe estar todo en mayúsculas.