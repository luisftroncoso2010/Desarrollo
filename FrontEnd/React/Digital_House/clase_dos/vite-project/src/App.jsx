import './App.css'
import { Home } from './pages/Home'
import { Navbar } from './Components/Navbar'
import { Form } from './Components/Form'
import {Routes, Route} from 'react-router-dom'
import { Concat } from './pages/Concat'
import { Cart } from './pages/Cart'
import { routes } from './utils/routes'
import { Details } from './pages/Details'

function App() {   
  return (
    <>
    {/* <Contex></Contex> */}
      <Navbar/>
      {/* <Form />
      <Home/>  */}
      <Routes>
        {/* Aca va el Home atraves de la ruta */}
        <Route path={routes.home} element={ <Home/> } />
        <Route path={routes.contac} element={<Concat/>} />
        <Route path={routes.cart} element={<Cart/>}/>
        <Route path='/detail/:id' element={<Details/>}/>
        <Route path='*' element={<h1>Error 404 - Page not found</h1> }/>
      </Routes>

    </>
  )
}

export default App
