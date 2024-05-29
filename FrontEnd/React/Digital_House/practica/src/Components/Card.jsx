import React from 'react'

const Card = ({cliente}) => {
    const { nombre, email } = cliente
  return (
    <div>
      <h3>Gracias: {cliente.nombre} </h3>
      <h4>Vas a recibir tu entra al email: {cliente.email} </h4>
    </div>
  )
}

export  { Card }
