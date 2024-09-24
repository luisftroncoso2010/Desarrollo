import logo from '../imagenes/freecodecamp-logo.png'
import '../styles/Logo.css'

const Logo = () => {
  return (    
    <div className='logo-contenedor'> 
        <img 
          src ={logo}
          className='logo'
          alt='Logo pagina' />
    </div>      
    
  )
}

export default Logo
