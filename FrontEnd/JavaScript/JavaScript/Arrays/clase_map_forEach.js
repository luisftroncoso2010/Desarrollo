//Methods that iterate over an array.
// Methods that DO NOT modify the original array (Immutability)

// map()
const numbers = [1, 2, 3, 4, 5]
const squaredNumbers = numbers.map(num => num * num)
console.log(numbers);
console.log(squaredNumbers);


// ForEach
numbers.forEach(element => {
    console.log(`Los elementos es: ${element}`);
    
});

const colors = ['Red', 'Pink', 'Blue']
const iteratedColors = colors.forEach(color => console.log(color))
console.log(colors);
console.log(iteratedColors);


// exercise: Fahrenheit to Celsious conversion
const tempraturesInFahrenheit = [32, 68, 95, 104, 212]
const tempreturesInCelsius = tempraturesInFahrenheit.map(fahrenheit => (5/9) * (fahrenheit - 32))
console.log(`Temperatures In Fanrenheit: ${tempraturesInFahrenheit}`);
console.log(`Tempratures In Celsius: ${tempreturesInCelsius}`);


// Exercise: Sum of elements in an Array
const newNumbers = [1, 2, 3, 4, 5]
let sum = 0
newNumbers.forEach(number => {
    sum += number
})

console.log("Sum of numbers: ", sum);
console.log("Array of numbers: ", newNumbers);




