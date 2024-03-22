// Imprime mensajes por consola
console.log("Hola mundo!")

// Mensaje de advertencia por consola
console.warn('Ocurrio un error')

// Muestra un mensaje de error
console.error('Ocurrio un error')

// Muestra donde ocurre un error
console.log(new Error('Error!'))

// Proceso
console.log(process.argv)
console.log(process.memoryUsage())

//Modulo Os
const os = require('os')
console.log(os.type())  // Muestra el sistema operativo
console.log(os.homedir())  // Muestra el usuario en que esta
console.log(os.uptime())  // Muestra el tiempo de estar ejecuentadi el sistema en segundos
console.log(os.userInfo())  // Informacion de usuario


console.log('-- setTimeout')
function mostrarTema(tema){
    console.log(`Estoy aprendiendo ${tema}`)
}


// Se ejecutará luego de 3 segundos
setTimeout(mostrarTema, 2000, 'Node.js')


function sumar(a, b){
    console.log(a + b)
}

// Sumamos dos valores y los mostramos luego de 3 segundos
setTimeout(sumar, 2000, 5,4)


console.log('-- setImmediate')


function mostrarTemaDos(tema){
    console.log(`Mostrar tema dos: ${tema}`)
}


console.log('Antes de setInmmedite()')
//setImmediate(mostrarTemaDos, 'TemaDos')
console.log('Despues de setImmediate()')


// setInterva
console.log('-- setInterval()')

function mostrarTemaTres(tema){
    console.log(`Mostrar tema Tres: ${tema}`)
}


//Se ejecutará el numero infinito de veces
//setInterval(mostrarTemaTres, 1500, 'Soy tema tres')
//setInterval(sumar, 1500, 3,4)


console.log('-- Modulo file system')  // Sistemas de archivos
const fs = require('fs')
const { error } = require('console')


// fs.readFile('inex.html', 'utf-8', (err, contenido) => {
//     if(err){
//         console.log(err)
//         throw error
//     } else{
//         console.log(contenido)
//     }
//     // Se seguira ejecutandose sin o hay error
//     console.log('mensaje...')
// })


console.log('-- rename')
// fs.rename('index.html', 'main.html', (err) =>{
//     if(err){
//         throw err
//     }
//     console.log('Nombre cambiado exitosamente. ')
// })

// Agregar contenido al final del archivo
fs.appendFile('index.html', '<p>Hola</p>', (err) =>{
    if(err){
        throw err
    }
    console.log('Archivo actualizado')
})


// Remplazar todo el contenido
fs.writeFile('index.html', 'Contenido nuevso', (err) => {
    if(err){
        throw err
    }
    console.log('Contenido Remplazando exitosamente')
})


// Eliminar archivos
fs.unlink('index.html', (err) => {
    if(err){
        throw err
    }
    console.log('Archivo eliminado')
})




