import { useState } from "react"
import { Envio } from "./Envio"
import { Button } from './Button'

const Form = () => {
  
  const [cliente, setCliente] = useState({
    nombre: '',
    direccion: ''
  }) 
  const [show, setShow] = useState(false)
  const [error, setError] = useState(false)

  // Se destructura el cliente
  const handleNombre = (e) => setCliente({...cliente, nombre: e.target.value})
  const handleDireccion = (e) => setCliente({...cliente, direccion: e.target.value})

  const handleSubmit = (e) => {    
    e.preventDefault()  
    if(cliente.nombre.trim().length > 3 && 
      cliente.direccion.trim().length > 5 && 
      cliente.direccion.includes(' ')){
      setShow(true)
      setError(false)  // No hay error
    } else{
      setError(true)
    }
  }  
  
  // const reset = () => {
  //   cliente.nombre('')
  //   cliente.direccion('')
  // }
  
  return (    
    <>
      <form onSubmit={handleSubmit}>
        <label >Nombre: </label>
        <input type='text' value={cliente.nombre} onChange={handleNombre}/>

        <label >Direccion: </label>
        <input type='text' value={cliente.direccion} onChange={handleDireccion}/>

        <Button>Enviar</Button>
      </form>

      { show && <Envio cliente={cliente} /> }   
      { error && (
        <p style={{color: 'red'}}>
          Debe colocar la infomacion correspondiente
        </p>     
        ) 
      } 
    </>
  )
}

export { Form }
