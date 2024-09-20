import './App.css';
import PropTypes from 'prop-types'

function App() {
  const usuario = {
    
    nombre: 'Luis',
    apellido: 'Díaz',
    edad: 18,
    genero: 'Masculino'
  }

  return (
    <div className="App">
      <Saludo usuario={usuario}></Saludo>
    </div>
  );
}

/* Creamos el componente que resibiría las props */
function Saludo(props){
  const {nombre, apellido, edad, genero} = props.usuario
  return(
    /* Validamos si la propiedad si existe o no. Debe de exister nombre y usuario a la ves, para mostrar todo el mensaje a la ves*/
      <div>{nombre && apellido ? (<div><h1>Hola {nombre} {apellido}!!</h1>
        <p>Tienes: {edad}</p>
        <p>Y tu género es: <strong>{genero}</strong></p></div>) : 
        <h1>No se ha proporcionado el nombre de usuario</h1> }
      </div>
  ) 
}

/* Validacion de datos de componentes */
Saludo.propTypes = {
  usuario: PropTypes.shape({
      nombre: PropTypes.string.isRequired,
      edad: PropTypes.number.isRequired
    })
}.isRequired;

export default App;
