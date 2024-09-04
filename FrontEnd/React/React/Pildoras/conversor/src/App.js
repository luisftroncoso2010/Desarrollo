
import './App.css';
import { useRef } from 'react';

function App() {

  const euroRef = useRef();
  const resultadoRef = useRef();

  const calcular = () => {
    const eurosValor = parseFloat(euroRef.current.value)
    const dolares = eurosValor * 1.11

    resultadoRef.current.innerHTML =  '$' + dolares.toFixed(2)
  }

  console.log(resultadoRef);
  

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
