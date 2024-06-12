import React, { useEffect, useState } from 'react'

const FuncComponentDos = () => {
    const [loading, setLoading] = useState(true)
    const [ nombre, setNombre]  = useState()
    console.log("Funcion Component") 
    
    useEffect(() => {
        console.log("Se montó el component") 
        setTimeout(() => {
            setTimeout(() => {  
                setLoading(false)              
            }, 3000);
        }, [loading])        
    }, []) 

    /* Use effec para cuando se actuliza una dependencia */
    useEffect(() => {
        if(!loading) setNombre('Pablo')
    }, [loading])

    /* Para cuando se desmonta el componente: Una accion que quieres 
    hacer antes de desmontar dicho componente
    */
    useEffect(() => {
        return () =>{
            console.log("se ejecuta cunaod se desmonta el componente");
        }
    }, [])
  return (
    <div>
      {loading ? 'Cargando..........' :
            <>
                <h3>Hola, {nombre}!</h3>
            </>
      }
    </div>
  )
}

export default FuncComponentDos
