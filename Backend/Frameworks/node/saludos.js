function saludar(nombre){
    return `Hola ${nombre}`
}

function saludarHolaMundo(){
    return '¡Hola Mundo!'
}

// Exportamos los elementos
// module.exports.saludar = saludar  // Asociamos a la funcion saludar
// module.exports.saludarHolaMundo = saludarHolaMundo


// Aca lo colocamos la exportaciones por medio de un objeto
module.exports = {
    saludar: saludar,
    saludarHolaMundo: saludarHolaMundo
}

