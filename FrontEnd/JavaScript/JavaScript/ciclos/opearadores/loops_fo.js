console.log("   * Loop: for");

let list = ['eat', 'sleep', 'code', 'repeat']

for (let index = 0; index < list.length; index++) {
    console.log(list[index]);
}

console.log("   * Loop: for of");
/* Se usa cuento hay objetos iterables */
for (const element of list) {
    console.log(element);   
}

console.log("   * Loop: for of");

/* Creamos un objeto */
const listaDeCompras = {
    manzanas: 5,
    pera: 3,
    naranja: 2,
    uva: 1
}

for (const key in list) {
    console.log(`Key del Objeto: ${key}. Este es el valor: ${list[key]}`);    
}

console.log('Lista de compras: ');
for (const key in listaDeCompras) {
    console.log(`Key lista de Compras: ${key}. Los elementos son: ${listaDeCompras[key]}`);
}


console.log("   * Loop: while");
/* While se ejecuta siempre y cuando sea true */
let contador = 0

while (contador < 10) {
    console.log(contador);   
    contador ++
}