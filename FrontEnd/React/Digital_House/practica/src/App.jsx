
import './App.css'
import { Espectaculo } from './Components/Espectaculo'
import { espectaculos } from './Utils/espectaculos'
import { Form } from './Components/Form'
import { useState } from 'react'

function App() {
  const [showForm, setShowForm] = useState(false)
  
  return (
    <>
      {espectaculos.map((item) => (
        <Espectaculo key={item.id}
         item={item}
         setShowForm={setShowForm} />
      ))}
      {showForm && <Form /> }
      
    </>
  )
}

export default App
