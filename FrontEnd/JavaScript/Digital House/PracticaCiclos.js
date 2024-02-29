let personajes = {
    nombre: "Luke",
    apellido: "Skywalker",
    edad: 25
}


// For in
for(let iteradora in personajes){
    console.table(`Key: ${iteradora} Valor: ${personajes[iteradora]}`);
}

// For of 
let series = ["La casa de papel", "The office", "Broklin 99"];
for(let nombreSeries of series){
    console.log(nombreSeries);
}