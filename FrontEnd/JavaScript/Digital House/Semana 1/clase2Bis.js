const nombreDelJugador = iniciarJuego()
let marcador = {
    usuario: 0,
    computadora: 0,
    empate: 0
}; 

// Mientras ninguno halla llegado a sumar dos puntos seguimos jugando
while(marcador.usuario < 2 && marcador.computadora < 2){
    const RESULTADO_PARTIDA = compararJugadas();
    alert(RESULTADO_PARTIDA);
    console.log(RESULTADO_PARTIDA);

    // Verificamos si gano o no
    if (RESULTADO_PARTIDA.includes("ganaste")) {
        marcador.usuario++;        
    } else if(RESULTADO_PARTIDA.includes("perdiste")){
        marcador.computadora++;        
    } else if(RESULTADO_PARTIDA.includes("empate")){
        marcador.empate++;
    }

    console.log(marcador);     
}


// Funcion para sumar valores de objetos
function sumaValObjetos(objeto){
    let suma = 0;
    for (let clave in objeto) {
        // Verificar si la propiedad realmente pertenece al objeto (no a la cadena de prototipo)
        if (marcador.hasOwnProperty(clave)) {
            suma += objeto[clave];  // Esto trae el valor que tiene
        }        
    }
    return suma;
}

// Instanciamos la variable para validar
let sumatotal = sumaValObjetos(marcador)
console.log(`La cantidad de partidas fueron: ${sumatotal}`)
console.log(`Ganadas: ${marcador.usuario}`);
console.log(`Perdidas: ${marcador.computadora}`);
console.log(`Empates: ${marcador.empate}`);