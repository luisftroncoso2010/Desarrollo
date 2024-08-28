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

// Objeto persona
const persona = {
    nombre: 'Jhon',
    edad: 30,
    direccion: {
        calle: 'Av Insurgentes 187',
        ciudad: 'CDMX'
    },
    saludar(){
        console.log(`Hola, mi nombre es ${persona.nombre}`);    
    }
}

console.log(persona);
persona.saludar()  // Aca mostramos la funcion saludar.


// Agregar propiedades
persona.telefono = '310-675-20-10'
console.log(persona);


// Agregar funciones al objeto
persona.despedir = () => {
    console.log('Adios');
}

persona.despedir()  // Imprimimos la funcion del objeto


// Delete propertis or methods
delete persona.edad;

delete persona.telefono;
console.log(persona);