const  almuerzo = (proteina, verduras) => {
    return `${proteina}, ${verduras}`
}
almuerzo('Pollo', 'Verduras')

// Function nomral,  return
const greethin = function(name){
    return `Hi, ${name}`
}


// Arrow function - explicit return
const newGreethin = (name) => {
    return `Hi, ${name}`
}

//  Arrow function - explicit return
const newGreethinImplicit = (name) =>  `Hi, ${name}`
const newGreethinImplicitTwoParameters = (name, lastName) => `Hi, I'am ${name} ${lastName}`


// Lexical Binding. 
const finctionalCharacter = {
    name: 'Uncle Ben',
    messageWhitTraditionalFunction: function(message){
        console.log(`${this.name} says: ${message}`);
    },
    messageWhitArrowFunction: (message) => {
        console.log(`${this.name} says: ${message}`);
    },
}

finctionalCharacter.messageWhitTraditionalFunction('With great power comes great responsability.')
finctionalCharacter.messageWhitArrowFunction('Beware of Doctor Octopus.')

console.log(' * Entorno Lexico:');
function createCounter(){
    let count = 0
    return function(){
        count++
        return count
    }
}

let counter = createCounter()
console.log(counter())
console.log(counter());


