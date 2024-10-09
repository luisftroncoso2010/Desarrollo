import parrafos from './Data/quijote.json'
import './App.css';
import { useState } from 'react'
import { Btn, Row } from './styles';
 
function App() {

  const [parrafoActual, setParrafoActual] = useState(0);

  const siguienteParrafo = () => {
    if(parrafoActual !== parrafos.length - 1) setParrafoActual(parrafoActual + 1)
  }

  const anteriorParrafo = () => {
    if(parrafoActual !== 0) setParrafoActual(parrafoActual - 1);
  }

  return (
    <div>
      <p> {parrafos[parrafoActual]} </p>
      
      <Row>
        <Btn onClick={anteriorParrafo}>Anterior</Btn>
        <Btn onClick={siguienteParrafo}>Siguiente</Btn>
      </Row>

    </div>
  
  );
}

export default App;
