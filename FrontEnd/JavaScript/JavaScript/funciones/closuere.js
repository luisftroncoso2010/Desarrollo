// Closuere: Función que tiene acceso a varables de un ámbito externo
// Ambito Lexico
function otherFuntion(){
    let outerVariable = "I am From outer function"
    function innterFuntion(){
        console.log(outerVariable);
    }
    return innterFuntion
}

// Closuer
const closureExample = otherFuntion()
closureExample()


// Clouser
function createCount(){
    let count = 0
    return function(){
        count ++
        console.log(`Contador: ${count}`);
        
    }
}

const counterA = createCount()
counterA()
counterA()

const counterB = createCount()
counterB()

/* Nota: Al ejecutar un Clouser seindo un contador
siempre "recuerda" el entorno en el que fue creada,
por ende sigue sumando en el caso del contador.
*/

// Diferentes tipos de contextos en los Closure
function outer(){
    let message = "Hello, "

    function innter(name) {
        console.log(message + name);
    }
    return innter
}


const clouserA = outer()
const clouserB = outer()

clouserA('Alice')
clouserB('Bob')
