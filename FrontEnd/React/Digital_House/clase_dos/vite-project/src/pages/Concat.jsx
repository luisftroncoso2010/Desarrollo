import React from 'react'

const Concat = ({onClick}) => {
  return (
    <form>
      <h1>Envianos tu consulta</h1>
      <input type="email" role='email' />
      <input type="text" data-testid = 'consulta' />
      <button onClick={onClick}> Enviar </button>
    </form>
  )
}

export  {Concat}
