import './App.css'
import  Navbar  from './Componentes/Navbar'
import  Footer  from './Componentes/Footer'
import { Outlet } from 'react-router-dom'

function App() { 

  return (
    <>
      <Navbar/> 
      <Outlet /> 
      <Footer />    
    </>
  )
}

export default App
