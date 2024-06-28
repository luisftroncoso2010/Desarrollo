import React, { useState } from 'react'
import { Button } from '../Components/Button'

const Concat = ({onClick}) => {

  const [estado, setEstado] = useState()

  return (
    <div>
      <h1>Envianos tu consulta</h1>
      <input type="email" role='email' />
      <input 
        type="text" 
        data-testid = 'consulta' 
        value={estado} 
        onChange={(e) => setEstado(e.target.value)} />
      <Button onClick={onClick}> Enviar </Button>
    </div>
  )
}

export  {Concat}
