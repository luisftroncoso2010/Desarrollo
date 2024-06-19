import React from 'react'
import { useParams } from 'react-router-dom'

const preguntas = [
    {    
        id: 1,
        title: "¿Puedo hacer el curso sin tener experiencia y/o conocimientos previos?",
        descripcion: "Sí. En Digital House puedes aprender desde cero. Según el curso al que te anotaste, vamos a enviarte contenido previo online..."
    },
    {
        id: 2,
        title: "¿Las vacantes son limitadas?",
        descripcion: "Sí. Tienen una capacidad máxima de entre 50 y 75vpersonas, dependiendo el curso."
    }    
]


const Faqs = () => {
   

    const params = useParams()
    console.log(params);

    // Convetimos a pasar el id de pregunta a entero
    const pregunta = preguntas.find(pregunta => pregunta.id === parseInt(params.id))

  return (
    <div> 
       <h1>FAQS: Desde pregunta especifica: {params.id} </h1>
       <section>            
            <h3>{pregunta?.title}</h3>
            <p>{pregunta?.descripcion}</p>
       </section>
       {/* <img src={Faqs} alt="Faqs"/> */}
    </div>
  )
}

export{ Faqs }