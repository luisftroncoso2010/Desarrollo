// Estotraerá el valor usando lapropiedad value
var nombre = document.getElementById("nombre").value
console.log(nombre)


var numero = document.getElementById("numero").value
console.log(numero)


//v Seleccionamos todos los elementos que tengan el mismo name
var elementos = document.getElementsByName("pregunta")

elementos.forEach(function(elemento){
    console.log(elemento)
    console.log(`Elementos: ${elemento.value}`)
    console.log(`Seleccionado: ${elemento.checked}`);
})


// Validamos el elementos privacidad
var privacidad = document.getElementById("privacidad")
console.log(privacidad)
console.log(`Elementos: ${privacidad.value}`)
console.log(`Seleccionado: ${privacidad.checked}`)
