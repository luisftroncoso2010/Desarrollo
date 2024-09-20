
import { useState } from 'react';
import './App.css';
import Boton from './componentes/boton';
import Contador from './componentes/Contador';
import logo from './imagenes/freecodecamp-logo.png'

function App() {

  const [numClics, setNumClics] = useState(0)

  /* Definir aplicacion dentro del componente */
  const manejarClic = () => {   
    console.log('Clic');    
    setNumClics(numClics + 1)
  };

  const reiniciarContador = () => {   
    console.log('Reiniciar contador');     
    setNumClics(0)
  };

  return (
    <div className="App">
      <div className='freecodecamp-logo-contenedor'>
        <img
          className='logo'
          src={logo}
          alt='Logo de Pagina'
          />
      </div>
      <div className='contenedor-principal'>
        <Contador numClics={numClics} />
        <Boton
          texto='Clic'
          esBotonDeClic={true}
          manejarClic={manejarClic} />
        
        <Boton
          texto='Reiniciar'
          esBotonDeClic={false}
          manejarClic={reiniciarContador} />
      </div>
    </div>
  );
}

export default App;
