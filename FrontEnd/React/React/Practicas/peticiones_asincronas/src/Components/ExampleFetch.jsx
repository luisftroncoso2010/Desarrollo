import axios from 'axios'
import  { React, useState, useEffect } from 'react'

const ExampleFetch = () => {
   const [perrito, setPerrito] = useState({})
    /* Se crea el endpoint donde se alamcena la respuesta de la api*/
   const endpoint = 'https://dog.ceo/api/breeds/image/random'  

   useEffect(() => {
    // fetch(endpoint)
    //     .then((response) => response.json())
    //     .then((data) =>setPerrito(data))
    //     .catch((err) => console.log(err)) 

    /* Esto nos arroja el objejo */
    axios(endpoint)
        .then((res) => setPerrito(res.data))  
        .catch(err => console.log(err))    
    }, [])

  return (
    <div>
      <img src={perrito.message}/>
    </div>
  )
}

export  {ExampleFetch}
