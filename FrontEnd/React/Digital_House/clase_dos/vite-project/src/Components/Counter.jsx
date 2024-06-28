import { useState } from 'react'
import { Button } from './Button'

const Counter = () => {    
    const [counter, setCounter] = useState(0)   

    const restar = () => {
        setCounter(counter - 1)
    } 

    const sumar = () => {
        /* Otra formade darle valor al estado es mediante
         un CALLBACK y traigo el valor del estaod por parametro */
        setCounter((prev) =>{        
            console.log('El valor de prev es: ', prev);
            return counter + 1
        })
    }        
        
  return (
    <div>        
      {/* <button onClick={restar} disabled={counter === 0}>-</button> */}
      <Button handleClick={restar}>-</Button>
      <h4>{counter}</h4>
      {/* <button onClick={sumar}>+</button> */}
      <Button handleClick={sumar}>+</Button>
    </div>
  )
}

export  { Counter }
