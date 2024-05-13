import PropTypes from 'prop-types';

const Estudiante = (props) => {
    console.log(props)    
    
    return (
        <div>
            <h3>Nombre: {props.nombre} </h3>
            <h4>Materia: {props.materia} </h4>
            <h5>Color favorito: {props.color} </h5>
            <br />
        </div>
    )
}

// Se oloca esto para que sea campos obligatorios
Estudiante.propTypes = {
    nombre: PropTypes.string.isRequired, 
    materia: PropTypes.string.isRequired,
    color: PropTypes.string.isRequired
  };

export { Estudiante}