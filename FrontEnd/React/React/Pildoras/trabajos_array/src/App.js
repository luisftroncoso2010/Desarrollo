import logo from './logo.svg';
import './App.css';

function App() {

  const miArray = () =>{
    /* Declaramos el array */
    const numerosArray = [
      {id: 1, numero: 18},
      {id: 2, numero: 18},
      {id: 3, numero: 10},
      {id: 4, numero: 15},
    ]
    /* Colocamos el elemento que devolverá la función */
    return(
      <p>{numerosArray.map((item) => {
        return <span key={item.id}>{item.id}:&nbsp;{item.numero}.&nbsp;</span>
      })}</p>
    )
  }

  return (
    <div className="App">
      <header className="App-header">
        <img src={logo} className="App-logo" alt="logo" />
        <h1>Numeros del Array: </h1>
        {miArray()}
      </header>
    </div>
  );
}

export default App;
