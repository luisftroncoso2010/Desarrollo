let nombre = 'Nico'

if (nombre === 'Diego') console.log('Hola Diego');   
else if (nombre === 'Nico') console.log("Hola nico");
else console.log(" Nombre no encontrado");   

console.log(" Juego: ");

const numeroSecreto = Math.floor(Math.random() * 10 + 1)
const numeroJugador = parseInt(prompt('Adivina el número secreto entre le 1 al 10 : '))

console.log(`Este es el número con el que juegs: ${numeroJugador}`);
if(numeroJugador === numeroSecreto)console.log('!Felecidades, adivinaste el número secreto¡');
else if (numeroJugador < numeroSecreto) console.log("El número es demasido bajo, intenta de nuevo");
else console.log("El número es muy alto, intenta de nuevo");


 
    
