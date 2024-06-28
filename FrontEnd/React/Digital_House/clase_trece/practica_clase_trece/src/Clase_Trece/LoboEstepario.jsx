import React from 'react'
import { useRecipeStates } from '../Contex/Context'

const LoboEstepario = () => {
    console.log('Se renderizó componente Lobo');

  const { salario } = useRecipeStates()

  return (
    <div className='lobo-estepario'>
      <img className='lobo' src='' alt='lobo' />
      {/* <h3>Total: { salario * 6 }</h3> */}
    </div>
  )
}

export  { LoboEstepario }
