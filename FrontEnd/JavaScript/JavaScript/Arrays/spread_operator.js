//1. Copy an Array
const originalArray = [1, 2, 3, 4]
const copyOfArray = [...originalArray]
console.log(originalArray);
console.log(copyOfArray);

// 2. Combining Arrays
const array1 = [1, 2, 3]
const array2 = [4, 5, 6]
const combiningArray = [...array1, ...array2]
console.log(array1);
console.log(array2);
console.log(combiningArray);


// 3. Creating Arrays with additional elements
const baseArray = [1, 2, 3]
const arrayWithaditionalElements = [...baseArray, 4, 5, 6]
console.log(baseArray);
console.log(arrayWithaditionalElements);

// 4. Pass elements to funtions 
function suma(a, b, c) {
    return a + b + c
}

const numbers = [1, 2, 3]
const result = suma(...numbers)
console.log('Array: ', numbers);
console.log('Sum of Array: ', result);


// 5. Strings 
const str = 'Hola Luis'
const charts = [...str]
console.log(charts);


// 


