import React from 'react'
import ReactDOM from 'react-dom/client'
import { BrowserRouter, Routes, Route} from 'react-router-dom'
import App from './App.jsx'
import './index.css'
import Home from './Componentes/Home.jsx'
import About from './Componentes/About.jsx'
import { Faqs } from './Componentes/Faqs.jsx'

ReactDOM.createRoot(document.getElementById('root')).render(
  <React.StrictMode>
    <BrowserRouter>
        <Routes>
          <Route path='/' element={<App/>}>
            <Route path='home' element={<Home/>}/>
            <Route path='about' element={<About/>}/>
            <Route path='/faqs/:id' element={<Faqs/>}/>      
          </Route>
        </Routes>
    </BrowserRouter>

  </React.StrictMode>,
)
