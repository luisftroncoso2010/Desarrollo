/*
Estructura de datos: Guarda valores de forma Key / Value
Forma: objeto {
    key/propiedad: valor,
    key/propiedad: valor,
    key/propiedad: valor,
    Metodos:
}
    Abstraer objetos de la realidad y llevarlo a la programación
*/

const persona = {
    nombre: 'Luis',
    edad: 27, 
    direccion: {
        calle: 'An Insurgentes 187',
        ciudad: 'CDMX'
    },
    saludar(){  // Acciones que hacen ls objetos invocarse
        console.log(`Hola mi nombre es ${persona.nombre}`);        
    }
}