import PropTypes from 'prop-types';

const Button = (props) => {

  return (
    <button onClick={props.funcion}> {props.texto} </button>
  )
}

Button.propTypes = {
  texto: PropTypes.string.isRequired, 
  funcion: PropTypes.func  
};

export  { Button }
