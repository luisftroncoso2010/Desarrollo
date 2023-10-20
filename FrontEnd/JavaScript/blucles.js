// bucles e iteracion  
let numero = 0;
let numero2 = 0;
let numero3 = 0;

document.write('----------- While------------------' + '<br>');

// Se coloca la condicion u luego se hace. 
while (numero < 6) {
    numero++;
    document.write(numero + "<br>");
};

document.write('-----Sentencia break dentro del While------' + "<br>");

while(numero3 < 100){
    numero3 ++;
    document.write(numero3 + "<br>");
    if(numero3 == 10){ //Se cierra al moemnteo de llegar a 10
        break;
    }
}

document.write('-----------Do While----------------' + "<br>");

// En el do while. Se coloca primero lo que se quiere que se muestre
// Luego se coloca la condicion 
do {
    numero2++;
    document.write(numero2 + "<br>");        
} 
while (numero2 < 5);

document.write('--For--' + "<br>");
// El ciclo for se divide en 3 partes. 
// declaracion e inicializacion de variables, condicion y aumento/decremento
for(let i = 0; i < 20; i++){    
    if(i == 12){
        continue;
    }
    document.write(i + "<br>");
};

document.write('--For en ARRAYS--' + "<br>");

let animales = ["Gato", "Perro", "Cocodrilo"];

for (animal in animales){
    document.write(animal + "<br>");
}

for (animal of animales){
    document.write(animal + "<br>");
}

document.write('----For en ARRAYS----' + "<br>");

array1 = ["Maria", "Josefa", "Roberta"];
array2 = ["Pedro", "Marcelo", array1, "Jose fina"];

for(let array in array2){ // in me trae el indice de las pocisiones
    if(array == 2){
        for(let array of array1){ // Este me recorre las posiciones y trae el dato
            document.write(array + "<br>")            
        }
    } else {
        document.write(array2[array] + "<br>")
    }
}



