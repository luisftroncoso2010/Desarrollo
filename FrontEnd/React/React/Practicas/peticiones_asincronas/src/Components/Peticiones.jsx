import { useEffect, useState } from "react"
import  _  from 'lodash'

const Peticiones = () => {    
    // useState
    const [vetor, setVetor] = useState([]);

    // Funcion para llamar los datos de la api
    const getData = async () => {
        const data = await
            fetch('https://jsonplaceholder.typicode.com/comments')
            const convert = await data.json();
            const elementosAleatorios = _.sampleSize(convert, 3)
            setVetor(elementosAleatorios)
    }

    useEffect(() => {
        getData()
    }, [])
  return (
    <div>
    <ul>
        {vetor.map(objeto => (<li key={objeto.id}>{objeto.email}</li>))}
    </ul>
    </div>
  )
}

export  { Peticiones }
