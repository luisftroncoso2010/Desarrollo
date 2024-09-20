import { MiCaja } from './style';
import { MiBotonLargo } from './styled2';


function App() { 
  return (
    <div className="App">
      <MiCaja entrar={false}>Entrar</MiCaja>
      <MiCaja entrar={true}>Salir</MiCaja>
      <MiBotonLargo>Salir</MiBotonLargo> 
    </div>
  );
}

export default App;
