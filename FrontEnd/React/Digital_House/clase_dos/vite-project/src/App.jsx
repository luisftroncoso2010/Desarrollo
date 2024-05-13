import './App.css'
import { Estudiante} from './Components/Estudiante'
import { Button } from './Components/Button'


function App() { 
  const borrar = () => {
    console.log('Se borro el elemento');
  }
  const cancelar = () => {
    console.log('Se cacelo la operacion');
  }
  const aceptar = () => {
    console.log('Se aceptaron los terminos y condiciones');
  }

  return (
    <>
     <h1>Hola luis, estas en React</h1>

     <Estudiante nombre='Andres' materia='Front'
      color='Black'/>
     <Estudiante nombre='Leo' materia='Back'
      color='Blue'/>
     <Estudiante nombre='Luis' materia='Dev'
      color='White'/>
     <Estudiante nombre='Juan' materia='Testing'
      color='Green'/>
      <Button texto='Cacelar' funcion={cancelar} />
      <Button texto='Borrar' funcion={borrar}/>
      <Button texto='Aceptar' funcion={aceptar}/>
     
    </>
  )
}

export default App
