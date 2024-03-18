/* --------------------------- NO TOCAR DESDE ACÁ --------------------------- */
let datosPersona = {
  nombre: "",
  edad: 0, 
  ciudad: "",
  interesPorJs: "",
};

const listado = [{
    imgUrl: "https://huguidugui.files.wordpress.com/2015/03/html1.png",
    lenguajes: "HTML y CSS",
    bimestre: "1er bimestre",
  },
  {
    imgUrl: "https://jherax.files.wordpress.com/2018/08/javascript_logo.png",
    lenguajes: "Javascript",
    bimestre: "2do bimestre",
  },
  {
    imgUrl: "https://upload.wikimedia.org/wikipedia/commons/thumb/4/47/React.svg/1200px-React.svg.png",
    lenguajes: "React JS",
    bimestre: "3er bimestre",
  },
];

const profileBtn = document.querySelector("#completar-perfil");
const materiasBtn = document.querySelector("#obtener-materias");
const verMasBtn = document.querySelector("#ver-mas");
const cambiarTema = document.querySelector('#cambiar-tema');

profileBtn.addEventListener("click", renderizarDatosUsuario)
materiasBtn.addEventListener("click", recorrerListadoYRenderizarTarjetas)

cambiarTema.addEventListener("click", alternarColorTema)
/* --------------------------- NO TOCAR HASTA ACÁ --------------------------- */

function obtenerDatosDelUsuario() {
  /* --------------- PUNTO 1: Escribe tu codigo a partir de aqui --------------- */ 
    // Declaramos la variables que nos interesan       
    let nombre = ""    
    let anioNacimiento, edadUsuario
    let ciudad
    let interesPorJs
    let soloNumeros 
    let soloLetras     
    let proceso = true
    
    
    // Nombre
    do {  
      soloLetras = /^[a-zA-Z]+$/      
      nombre = prompt("Nombre: ")   
  
      if (nombre === null) {
        // El usuario presionó Cancelar, salimos del bucle
        alert("Presionaste cancelar")
        proceso = false
        break
      }     
      
      if (!soloLetras.test(nombre)) {
        alert("Por favor, use un nombre mayor a tres letras y NO use números.")        
      } else {
        proceso = true
        break
      }
    } while(proceso)


    // Edad
    if (proceso) {
      do {
      soloNumeros = /^[0-9]+$/;
      const anioNacimiento = prompt("Año de nacimiento: ")

      if (anioNacimiento === null) {
        // El usuario presionó Cancelar, salimos del bucle.
        alert("Presionaste cancelar");
        proceso = false;
        break;
      }

      let anioDeNacimiento = parseInt(anioNacimiento)
      let anioActual = new Date().getFullYear()
      edadUsuario = anioActual - anioDeNacimiento
      

      if (isNaN(edadUsuario) || edadUsuario < 18 || !soloNumeros.test(anioNacimiento)) {
        alert("Por favor, use una edad válida mayor que 17 y NO use letras");
      } else {
        proceso = true;
        break;
      }
      } while (proceso);
    }
           
    
    // Ciudad
    if(proceso){
      do {  
      soloLetras = /^[a-zA-Z]+$/      
      ciudad = prompt("Ciudad: ")      
   
      if (ciudad === null) {
        // El usuario presionó Cancelar, salimos del bucle
        alert("Presionaste cancelar")
        proceso = false
        break
      }     
        
      if (ciudad.length < 3 || !soloLetras.test(ciudad)) {
        alert("Por favor, use un nombre de ciudad correcta.")        
      } else {
        proceso = true
        break
      }  
      } while(proceso)
    }


    // Interes por JavaScript
    if(proceso){
    do {  
      soloLetras = /^[a-zA-Z]+$/      
      interesPorJs = prompt("Interes por JavaScript: ")      
   
      if (interesPorJs === null) {
        // El usuario presionó Cancelar, salimos del bucle
        alert("Presionaste cancelar")
        proceso = false
        break
      }     
        
      if (interesPorJs.length < 1) {
        alert("Por favor, coloque el interes que tiene en el lenguaje de programacion")        
      } else {
        proceso = true
        break
      }  
    } while(proceso)
    }
    
    // Pruebas en el navegador.
    if (nombre !== null && edadUsuario !== null && ciudad !== null && interesPorJs !== null) {
      // El usuario no presionó Cancelar, realizamos acciones adicionales si es necesario
      nombre = nombre.charAt(0).toUpperCase() + nombre.slice(1).toLowerCase()
      ciudad = ciudad.charAt(0).toUpperCase() + ciudad.slice(1).toLowerCase()
      interesPorJs = interesPorJs.charAt(0).toUpperCase() + interesPorJs.slice(1).toLowerCase()
      console.log(`Nombre: ${nombre}, Edad: ${edadUsuario}, Ciudad: ${ciudad}, Interes Por JavaScript: ${interesPorJs}`)
    }


    // Almacenamos los datos recogidos en el objeto
    datosPersona.nombre = nombre
    datosPersona.edad = edadUsuario
    datosPersona.ciudad = ciudad
    datosPersona.interesPorJs = interesPorJs
    console.log(datosPersona) 

} 


function renderizarDatosUsuario() {
  /* ------------------- NO TOCAR NI ELIMINAR ESTA FUNCION. ------------------- */
  obtenerDatosDelUsuario();
  /* --------------- PUNTO 2: Escribe tu codigo a partir de aqui --------------- */
  // Capturamos las etiquetas atraves de un selector
  const nombre_ = document.querySelector('#nombre')
  const edad_ = document.querySelector('#edad')
  const ciudad_ = document.querySelector('#ciudad')
  const interesJs = document.querySelector('#javascript')

  // Insertar el dato en el html, atraves del selector
  nombre_.textContent = datosPersona.nombre
  edad_.textContent = datosPersona.edad
  ciudad_.textContent = datosPersona.ciudad
  interesJs.textContent = datosPersona.interesPorJs; 
   
}


let mostrarTarjetas = false
function recorrerListadoYRenderizarTarjetas() {
  /* ------------------ PUNTO 3: Escribe tu codigo desde aqui ------------------ */
  const fila = document.querySelector('#fila')
  
  fila.innerHTML = " "
  if(mostrarTarjetas){
    listado.forEach(lista => {
    fila.innerHTML += `
    <section class="caja">
      <img src="${lista.imgUrl}" alt="${lista.lenguajes}">
      <p>${lista.lenguajes}</p>
      <p>${lista.bimestre}</p>
    </section>
    `   
    })
  }    
  // Alternar el estado para el próximo clic
  mostrarTarjetas = !mostrarTarjetas;
}

function alternarColorTema() {
  /* --------------------- PUNTO 4: Escribe tu codigo aqui --------------------- */
  const idSitio = document.querySelector('#sitio');
  return idSitio.classList.toggle("dark") 
}



/* --------------------- PUNTO 5: Escribe tu codigo aqui --------------------- */
// Creamos el evento
window.addEventListener("keydown", eliminarClase)
function eliminarClase(evento){

  // Capturamos el selector que no tiene clase
  let claseOculta = document.querySelector("#sobre-mi")  

  // Presionanamos F PAra eliminar la clase
  if(evento.code == "KeyF"){   
    claseOculta.classList.remove("oculto")

  // Plus para volver a colocar la clase eliminada  
  }else if (evento.code == "KeyA" && !claseOculta.classList.contains("miClase")) {    
    claseOculta.classList.add("oculto");
  }  
}
