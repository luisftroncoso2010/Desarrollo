// Methods that iterate over an array
// Methods that DOT NOt modify the array original array (Inmutability)

// Filter()
const numbers = [2, 4, 5, 6, 7, 8, 9, 10]
const eventNumbers = numbers.filter(number => number % 2 == 0)
console.log("Arrays Original: ", numbers);
console.log("Numeros para del Array: ", eventNumbers);


// reduce() - Case 1
const numberReduce = [1, 2, 3, 4, 5]
/* Esta funcion reciber dos parametros */
const sum = numberReduce.reduce((accumulator, currenValue) => accumulator + currenValue, 0)
console.log(numberReduce);
console.log(sum);


// reduce() - Case 2
const words = ['Apple', 'Banana', 'Hello', 'Bye', 'Banana', 'Bye', 'Bye']
const wordFrecuency = words.reduce((accumulator, currenValue) => {
    if(accumulator[currenValue]){
        accumulator[currenValue]++
    }else{
        accumulator[currenValue] = 1
    }   
    return accumulator
}, {})  // Se debe colocar el objeto para alamcenar el objeto clave - valor

console.log(wordFrecuency);