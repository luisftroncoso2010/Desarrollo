function iniciarJuego(){
    // Saludar al visitante
    alert("Bienvenido al juego de piedra papel o tijeras de Frontend");    
    let nombre;
    do {
        nombre = prompt("Me puede indicar su nombre: ").trim();
        if(!(/^[a-zA-Z]+$/.test(nombre) && nombre.length >= 3)){
            alert("Por favor ingrese un nombre con eltamaño de letras valido")
        }else{
           nombre = nombre.toLocaleUpperCase();
        }        
        
    } while (!(/^[a-zA-Z]+$/.test(nombre) && nombre.length >= 3));

    // MOstrando datos por consola 
    console.log(`---------------------`);
    console.log(`El nombre del jugador es: `);
    console.log(nombre.toLocaleUpperCase());
    console.log(`---------------------`);

    return nombre.toLocaleUpperCase();
}

iniciarJuego();


/* -------------------------------------------------------------------------- */
/*                          CONSIGNA                          */
/* -------------------------------------------------------------------------- */
// 1- Modificar la funcion de iniciarJuego(), validar si ingresa un dato válido como nombre.
// 2- Si no ingresa un texto, o tiene menos de 3 caracteres debemos volverle a pedir que lo ingrese.
// 3- Finalmente el nombre devuelto debe estar todo en mayúsculas.