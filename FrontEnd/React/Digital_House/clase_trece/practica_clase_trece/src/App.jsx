import { useState } from 'react'
import { ParentComponent } from './Clase_Trece/ParentComponent'
import { LoboEstepario } from './Clase_Trece/LoboEstepario'
import './App.css'

function App() {
  const [count, setCount] = useState(0)

  return (
    <>    
      <ParentComponent/>
      <LoboEstepario/>    
    </>
  )
}

export default App
