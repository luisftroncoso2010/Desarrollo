console.log(document);

// Obtenr el titulo principal
const  titulo = document.querySelector("h1");
console.log(titulo);
console.log(titulo.textContent)

// Leer los atriburtos de ls etiquetas atraves de las clases y elementos
const itemsMenu = document.querySelector(".info");
const infoClima = document.querySelector(".info .clima");
const navItems = document.querySelector("ul li");
const image = document.querySelector("[src='./img/futbol.webp']");
console.log(image);


// Iterar a los articulos (articles)
const articulos = document.querySelectorAll("article");
console.log(articulos);


console.log("-- Capturamos todos los textos de los articles --")
// Iteramos dentro de las lista de articulos o que tiene dentro
for(let i = 0; i < articulos.length; i++){
    console.log(articulos[i].innerText);  // Capta todo el texto que este 
}


// Buscamos solo los titulos h2
console.log("-- Buscamos los articulos --");
articulos.forEach(articulo => {
    const titulo = articulo.querySelector("h2").textContent;  // Captura el texto plano
    console.log(titulo);    
});


console.log("-- Buscamos los iten menus --");
const menuItems = document.querySelectorAll("ul li");
console.log(menuItems);
console.log(menuItems[0].style.textTransform = "uppercase");  // Pasamos la letra mayúsculas

console.log("-- Pasamos la letra a mayusculas. Hacemos cambios a todos los elementos items --")
menuItems.forEach(item => {
    item.style.textTransform = "uppercase";
    item.style.color = "aqua";
    item.style.backgroundColor = "rgba(255, 255, 255, 0.2)";
    item.style.borderRadius = "50vh";
    item.style.padding = "10px";
    item.style.margin = "10px";
    item.style.marginTop = "20px";        
});


// capturamos el body
const sitio = document.querySelector("body");
console.log(sitio);

// Le damoa una nueva clase para que le siitio la tome, con relacion a los 
console.log(sitio.classList.add("dark"));  
/* Validamos si tiene la clase "dark" (contains es booleano)
tougle: Para ti tiene la clase o no, si la tiene la quita y 
si no la tiene la coloca
*/
console.log(sitio.classList.contains("dark"));  // Validamos si tiene la clase o no.
console.log(sitio.classList.toggle("dark"));

