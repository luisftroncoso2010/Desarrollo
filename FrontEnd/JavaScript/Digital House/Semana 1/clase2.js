function pedirJugada(){
    // Elecccion para juego
    let eleccion = 0;
    do {
        // Pedir que elija una opcion valida
        // convertir el texto que nos llega a un entero
        // reemplazar el valor guardado en la variable
        eleccion = parseInt(prompt("Ingrese para jugar 1(🗿 Piedra) 2(🧻 Papel) o 3(✂️Tijera)"))
        
        } while (isNaN(eleccion) || eleccion < 1 || eleccion > 3);
    
        // para mostrar por consola
        console.log("-----------------");
        console.log("La elección del jugador es:");
        console.log(eleccion);
        console.log("-----------------");
    
        return eleccion
}


function jugarRandom(){
    min = 1;
    max = 4;
    let numero = parseInt(Math.random() * (max - min) + min);
    console.log("-------------");
    console.log("La eleccion del PC es: ");
    console.log(numero);
    console.log("-------------");

    // Retorno el numero de la eleccion aleatoria
    return numero;    
}


function compararJugadas(){
    const RESULTADOS_POSIBLES = ["Genial, ganaste", "Esto fue un empate", "Que lastima perdiste!"];
    const OPCIONES = ["Piedra", "Papel", "Tijeras"];

    const ELECCIONJUGADOR = pedirJugada();
    const JUGADA_PC = jugarRandom();

    // Valor por defecto de la jugada es ganste
    let resultadoRonda = RESULTADOS_POSIBLES[0];

    // Cambiar el resultado de la ronda... si empata o pierde
    if (ELECCIONJUGADOR == JUGADA_PC) {
        resultadoRonda = RESULTADOS_POSIBLES[1];
    } else if (
        (ELECCIONJUGADOR == 1 && JUGADA_PC == 2) ||
        (ELECCIONJUGADOR == 2 && JUGADA_PC == 3) ||
        (ELECCIONJUGADOR == 3 && JUGADA_PC == 1)
        ) {
            resultadoRonda = RESULTADOS_POSIBLES[2];                    
    }

    return `La PC eligio: ${OPCIONES[JUGADA_PC - 1]} \nEleccion Jugador: ${OPCIONES[ELECCIONJUGADOR - 1]} \n${resultadoRonda}`
}

