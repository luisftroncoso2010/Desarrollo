
import './App.css'; 
//import Tarea from './componentes/Tarea'
 
import ListaDeTareas from './componentes/ListaDeTareas';
import freecodecamplogo from './imagenes/freecodecamp-logo.png'

function App() {
  return (
    <div className="aplicacion-tareas">
      <div className='freecodecamp-logo-contenedor'>
        <img src={ freecodecamplogo }
         alt='Logo FreeCodeCamp'
         className='freecodecamp-logo'
        />
      </div>
      <div className='tareas-lista-principal'>
        <h1>Mis Tareas</h1>  
        <ListaDeTareas />
        
      </div>
    </div>
    
  );
}

export default App;
