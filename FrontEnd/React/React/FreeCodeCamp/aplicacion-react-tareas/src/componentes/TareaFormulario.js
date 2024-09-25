import { useState } from 'react'
import '../hojas-de-estilo/TareaFromulario.css'
import { v4 as uuidv4 } from 'uuid'

function TareaFormulario(props){

    const [input, setInput] = useState('')

    const manejarCambio = e => {        
        /* Maneja el valor del texto escrtio en el input */
        setInput(e.target.value)                
    };

    const manejarEnvio = e => {
        e.preventDefault()     
        
        const tareaNueva = {
            id: uuidv4(),
            texto: input,
            completada: false
        };
        /* Se usa onsubmit cuando el formulario se envie */
        props.onSubmit(tareaNueva)
    };

  return (
    <form className='tarea-formulario'
        onSubmit={manejarEnvio}
    >
        <input className='tarea-input' 
            type='text'
            placeholder='Escribe una Tarea'
            name='texto'
            onChange={manejarCambio}
        />    
        <button className='tarea-boton'>
            Agregar Tarea
        </button>          
    </form>
  )
};



export default TareaFormulario
