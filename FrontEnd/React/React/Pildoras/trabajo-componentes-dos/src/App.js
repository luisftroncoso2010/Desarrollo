import './App.css';
import PropTypes from 'prop-types'

function App() {
  const usuario = {
    nombre: 'Luis',
    apellido: 'Díaz',
    edad: "18",
    genero: 'Masculino'
  }

  return (
    <div className="App">
      <Saludo usuario={usuario} ></Saludo>
    </div>
  );
}

/* Creamos el componente que resibiría las props */
function Saludo(props){
  return(
      <div>
        <h1>Hola {props.usuario.nombre} {props.usuario.apellido}!! </h1>
        <p>Tienes: {props.usuario.edad}</p>
        <p>Y tu género es: <strong>{props.usuario.genero}</strong></p>
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
