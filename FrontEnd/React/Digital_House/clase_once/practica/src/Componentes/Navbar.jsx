import React from 'react'
import  { Link } from "react-router-dom"
import Home from './Home'


const Navbar = () => {
  return (
    <>
     <nav>      
       <Link to="./Home" > Home </Link>
       <Link to="/About" > About </Link>
       <Link to="/Faqs" > Faqs </Link>
     </nav>     
    </>
  )
}

export default Navbar
