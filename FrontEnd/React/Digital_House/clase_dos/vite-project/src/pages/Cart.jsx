import React from 'react'
import { Form } from '../Components/Form'
import { useRecipesStates } from '../context/Context'
import { Card } from '../Components/Card'

const Cart = () => {
  const { cart } = useRecipesStates()
  return (

    <div>
      <h2>Pizzas seleccionadas</h2>
      <div className='list-container'>
       { cart.map((pedido) => 
        <Card key={pedido.id} item={pedido} />
      )}
      </div>  
      <Form />   
    </div>
  )
}

export  {Cart}
