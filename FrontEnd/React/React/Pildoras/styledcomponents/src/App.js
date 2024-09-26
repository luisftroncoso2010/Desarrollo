import { MiCaja } from './style';
import { MiBotonLargo } from './styled2';

function App() { 
  return (
    <div className="App">
      <MiCaja entrar={true}>Entrar</MiCaja>
      <MiCaja entrar={true}>Salir</MiCaja>
      <MiBotonLargo entrar={true}>Salir</MiBotonLargo> 
    </div>
  );
}

export default App;
