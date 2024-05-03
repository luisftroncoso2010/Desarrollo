let a = 1
var b = 2
const c = 3

function scopeVar(){
    if(true){
        var x = 10
        console.log(x)
    }
    console.log(x)
}

scopeVar()

const scopeLet = () => {
    if(true){
        let y = 20
        console.log(y)
    }
    // console.log(y)
}
scopeLet()

let frutas = ['Ciruelas', 'Melon', 'Uvas']
let verduras = ['Zanahoria', 'Zapallo', 'Tomate']

console.log(frutas[1])
frutas.push('Mazana')
console.log(frutas)
frutas.pop()  // Borra el ultimo elemento
console.log(frutas)
frutas.shift()  // Elimina el primer elemento
console.log(frutas)  

const verdureria =  [...frutas, ...verduras]  // Devuelve una matriz cuando es sin spret. Con el spret devuelve una matriz entera
console.log(verdureria)


const estudiante = {
    nombre: 'Diego',
    materia: 'Front End',
    location: 'Colombia'
}
console.log(estudiante)  // Muestra todo el objeto
estudiante.nombre = 'Luis'  // Cambiamos el nombre del estudiante
console.log(estudiante) 

const persona = {
    status: 'Termiminado',
    mascota: 'Perro',
    ...estudiante
}
console.log(persona)


