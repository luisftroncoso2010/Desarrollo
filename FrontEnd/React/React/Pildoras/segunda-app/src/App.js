import './App.css';
import { useState } from 'react';

/* Esto es un componente */
function App() {
  
  /* Definir el estado para alamacenar el resultado */
  const [resultado, setResultado] = useState(null)  
  const elementoDos = suma(5, 7)

  const botonPulsado = () => {    
    setResultado(elementoDos)
  }
  
  return (
    <div className='centrar-titulo'>
        <button onClick={botonPulsado}>Púlsame</button>
        <h1 >Hola mundo</h1>
        {/* Solo me mostrará el texto siempre que haya valor en resultado */}
        <div>{resultado != null && <h2>El resultado es: {resultado}</h2>}</div> 
    </div>
  )
}


/* Tenemos una funcion debajo del compnente */
function suma(a, b) {
  return a + b
} 

export default App;
