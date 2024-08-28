// Inmutabilidad
const fruits = Array('Apple', 'Banana', 'Orange')
console.log(fruits);


// Mutability
fruits.push('Watermelon')
console.log('Nuevo Array', fruits);


// Inmutability
const newFruits = fruits.concat(['Grape', 'Kiwi'])
console.log(fruits);
console.log(newFruits);


// Checking arrays with Array.isArray
const isArray = Array.isArray(fruits)
console.log(isArray);


// Practical exercise: sum all element of an array
const numberArray = [1, 2, 3, 4, 5]
let sum = 0

for(let i = 0; i < numberArray.length; i++){
    sum += numberArray[i]
}

console.log('Suma del Array:', sum);


