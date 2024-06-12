import React, { useEffect, useState } from 'react'

const FuncComponent = () => {  
    /* Esdta se crea el estado */
   const [loading, setLoading] = useState(false)
   const [counter, setCounter] = useState(0)   

   console.log("Funcion Component")  
   
   useEffect(() => {
    console.log("Efecto - contador") 
    setCounter(counter + 1)
   }, [loading])   
 
   return (    
    <div> 
        <h1>Componentes de Funcion</h1>
        { console.log("Render Component Funcional") }   
        {loading ? counter :  null}
        <br />        
        <button onClick={() => setLoading(!loading)}> Cargar contador</button>  
    </div>
  )
}

export default FuncComponent 
