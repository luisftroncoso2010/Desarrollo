import './App.css';

/* Esto es un componente */
function App() {
  
  
  const elementoDos = suma(5, 7)
  
  return (
    <div className='centrar-titulo'>
        <h1 >Hola mundo</h1>
        <p>{elementoDos}</p> 
    </div>
  )
}


/* Tenemos una funcion debajo del compnente */
function suma(a, b) {
  return a + b
} 

export default App;
