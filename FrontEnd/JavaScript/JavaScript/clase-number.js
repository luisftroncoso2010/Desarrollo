/* Clase de tipo de dato primitivo number */
// 1. Tipo entero y decimal

const entero = 42
const decimal = 3.14
console.log(typeof entero, typeof decimal);

// 2. Notación cientifica
const cientifico = 5e3
console.log(cientifico);


// 3. Infinitos y Nan
const infinito = Infinity
const noEsUnNumero = NaN


/* Operaciones aritméticas */
/* 1. suma, resta, Multiplicación y División */
const suma = 3 + 4
const resta = 4 - 4
const multiplicacion = 4 * 7
const division = 16 / 2

// 2. Módulo Exponenciación 
const modulo = 15 % 8
const exponenciacion = 2 ** 3

// Precisión
const resultado = 0.1 + 0.2
console.log(resultado);
console.log(resultado.toFixed(1));  // Me muestra un solo decimal
console.log(resultado === 0.3);  // Esto da false a nivel de tipo y numero


console.log(' * Operaciones Avanzadas: ');

const raizCuadrada = Math.sqrt(16)  // Raiz Cuadrada
const valorAbsoluto = Math.abs(-7)  //Valor abosoluto
const aleatorio = Math.random();  // Genera numeros aletorioa entre 0 y 1
console.log(raizCuadrada);
console.log(valorAbsoluto);
console.log(aleatorio);


