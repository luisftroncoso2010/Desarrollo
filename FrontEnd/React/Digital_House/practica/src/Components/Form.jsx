import { useState } from "react"
import { Card } from './Card'
import { ErrorMessage } from './ErrorMessage'

const Form = () => {

    const [cliente, setCliente ] = useState({
        nombre: '',
        email: ''
    })

    const [show, setShow] = useState(false)
    const [error, setError] = useState(false)


    const handleSubmit = (e) => {
        e.preventDefault()
        const regex = /^[\w-\.]+@([\w-]+\.)+[\w-]{2,4}$/g
        if(cliente.nombre.trim().length > 5 && regex.test(cliente.email)){
            setShow(true)
            setError(false)
        } else{
            setError(true)
        }
    }


  return (
    <>
        <form onSubmit={handleSubmit}>
            <label>Nombre del titular:</label>
            <input type="text" 
             onChange={(e) => setCliente({...cliente, nombre: e.target.value})} 
            />
            
            <label >Email: </label>
            <input type="text"
             onChange={(e) => setCliente({...cliente, email: e.target.value})}
            />
            <button>Finalizar Compra</button>
        </form>
        {show && <Card cliente={cliente} />}
        {error && <ErrorMessage />}
      
    </>
  )
}

export {Form}
