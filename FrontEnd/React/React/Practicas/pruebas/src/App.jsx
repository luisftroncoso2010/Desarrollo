import { useState } from 'react'
import './App.css'
import ClassComponent from './componentes/ClassComponent'
import FuncComponent from './componentes/FuncComponent'
import FuncComponentDos from './componentes/FuncComponentDos'

function App() {
  const [toggle, setToggle] = useState(true)

  return (
    <>
      {toggle && <FuncComponentDos />}
      <button onClick={() => setToggle(!toggle)}>
        {toggle ? 'Borrar' : 'Montar '} Componente
      </button>
      <br />
     <ClassComponent />
     <br />
     <FuncComponent />     
          
    </>
  )
}
export default App
