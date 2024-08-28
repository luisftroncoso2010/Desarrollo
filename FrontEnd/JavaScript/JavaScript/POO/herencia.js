class Animal{
    // Constructor de clase
    constructor(nombre, tipo){
        this.nombre = nombre;
        this.tipo = tipo
    }
    // Metodos
    emitirSonido(){
        console.log('EL animal emite un sonido');
    }

}

class Perro extends Animal{
    //Constructor
    constructor(nombre, tipo, raza){
        // PCon esto se pueden entrar a la propieda des de la clase padre
        super(nombre, tipo);
        // Llama el contructor de la clase Base
        this.raza = raza
    }
    emitirSonido(){
        console.log(`El perro ${this.nombre} Ladra`);   
    }

    correr(){
        console.log(`${this.nombre} corre alegremente`);
    }
}

// Creamos la instancia
const perroUno = new Perro('Lucas', 'Perro', 'Labrador')
console.log(perroUno);
perroUno.correr()
perroUno.emitirSonido()

console.log(Animal.prototype);
console.log();


