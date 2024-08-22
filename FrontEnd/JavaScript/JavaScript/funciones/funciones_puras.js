// Funciones puras


// Side Effects
/* 1. Modi ficar variables globales 
2. Modificar los parametros de una función
3. Solicitudes Https
4. Imprimir mensjaes en la pantalla o en el codigo
5.  Manimilacion dom DOM
6. Acceder a la hora actual
Nota: No siempre es malo, solo es dejarlos simepre. Por ejemplo de puede probar

*/

/* Funciones impuras */
function sum(a, b){
    console.log(`A: ${a}`);
    return a + b
}
// For ezample
let total = 0

function sumWithSideEffect(a){
    total += + a 
    return total
}

// For example. Función pura
function square(x){
    return x * x
}

function addTen(y){
    return y + 10
}

/* Funciones puras. El uso de dos funciones puras al mismo tiempo */
const number = 5
const finalReult = addTen(square(number))
console.log(finalReult);

