/* Creación de clases */
class Persona{
    constructor(nombre, edad){
        this.nombre = nombre,
        this.edad = edad
    }
    saludar(){
        console.log(`Hola. Mi nombre es ${this.nombre} y tengo ${this.edad}`);
    }
}

/* Creamoa el objeto de tipo Persona */
const personaUno = new Persona('Luis', 27)
console.log(personaUno);
/* Imprimimos la funcion atraves del objeto, saludar. */
personaUno.saludar()

