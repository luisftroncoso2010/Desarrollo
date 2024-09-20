
import './App.css';
import { useRef, useState, useEffect } from 'react';

function App() {
  /*Al macenamos la tasa de cambio */
  const [valorCambio, setValorCambio] = useState(null);

  const euroRef = useRef();
  const resultadoRef = useRef();

  /* Hacemos operación asincrona. Usea effect. Llamar la api, hacer solicitudes http */
  useEffect(() => {
    const llamaApiCambio = async() => {
       /* Ejecutamos el lboque try-catch para valida la tarea */
      try {
        const respuesta = await fetch('https://v6.exchangerate-api.com/v6/4cc111268081b395eb09468f/latest/USD')
        const datos = await respuesta.json()

        /* Muestra el Json por consola */
        console.log(datos);
        
        /* Accesedemos a la tasa de valor cambio */
        setValorCambio(datos.conversion_rates.EUR)
        
      } catch (error) {
        /* Dado el caso que no traiga nada o haya error mostrará este mensaje */
        console.log('Error al acceder a la API: ', error)
      }
    }
    llamaApiCambio()   
  }, [])

  const calcular = () => {
    const eurosValor = parseFloat(euroRef.current.value)
    const dolares = eurosValor * valorCambio

    resultadoRef.current.innerHTML =  '$' + dolares.toFixed(2)
  }
  // console.log(euroRef);
  // console.log(resultadoRef);
  // console.log(valorCambio);
  // console.log(setValorCambio);
  
  return (
    <div className="App">
      
      <h1>Conversor De Dolar a Euros</h1>
      <input type='text' ref={euroRef}></input>      
      <button onClick={calcular}>Convertir</button>
      <div className='resultado' ref={resultadoRef}></div>

    </div>
  );
}

export default App;
