import React, { useState } from 'react'
import { useRecipeStates } from '../Contex/Context'

const ChildComponent = () => {
    
const { salario, setSalario } = useRecipeStates()

  console.log('Se renderizó componente Hijo')

  const click = () => {
    return setSalario(salario + 60)
  }
    
  return (
    <div className='child'>
      <h3>Child Component</h3>
      <p>¿Cuanto ganas por semestre?</p>
      <h3> Total: {salario} </h3>
      <button onClick={click}>Aumente mi salario</button>
    </div>
  )
}

export { ChildComponent }
