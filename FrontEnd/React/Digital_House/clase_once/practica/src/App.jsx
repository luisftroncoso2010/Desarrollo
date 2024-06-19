import './App.css'
import  Navbar  from './Componentes/Navbar'
import  Footer  from './Componentes/Footer'
import { Outlet, useNavigate } from 'react-router-dom'

function App() { 
  const navigate = useNavigate()

  const handleClick = () => {
    navigate('/Home')
  }

  return (
    <>      
      <Navbar/> 
      <Outlet /> 
      <Footer /> 
      <br />
      <button onClick={handleClick}> 
       Go Home
      </button>   

    </>
  )
}

export default App
