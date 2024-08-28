/* Funcion constructora de objetos */

// const persona = {
//     nombre: 'Diego',
//     apellido: 'De Granda',
// }

// Funcion que construlle objetos
function Personas(nombre, apellido, edad) {
    // This hace referencia a este objeto
    this.nombre = nombre;
    this.apellido = apellido;
    this.edad = edad;
}
// Creamos los objetos
const personaUno = new Personas('Juan', 'Perez', 30)
const personaDos = new Personas('Luis', 'Gomez', 40)
console.log(personaUno);
console.log(personaDos);

/* NOTA: Esto no se agrega a la funcion constructora, si no al Prototype */
Personas.prototype.telefono = '310-675-2010'

/* Agragamos una propiedad a una instancia o objeto creado */
personaUno.nacionalidad = 'Mexicano';
console.log(personaUno);

/* Agregamos funciones al objetos de tipo "Constructor" */
Personas.prototype.saludar = function(){
    console.log(`Hola. Me llamo ${this.nombre} ${this.apellido}`);
}
personaUno.saludar()
console.log(personaUno);
