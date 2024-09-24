import '../styles/BotonClear.css'

const BontonClear = (props) => {
  return (
    <div className='boton-clear'
      onClick={props.manejarClear} >
      {props.children}
      
    </div>
  )
}

export default BontonClear
