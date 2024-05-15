import { useState } from 'react'

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
      <button onClick={restar} disabled={counter === 0}>-</button>
      <h4>{counter}</h4>
      <button onClick={sumar}>+</button>
    </div>
  )
}

export  { Counter }
