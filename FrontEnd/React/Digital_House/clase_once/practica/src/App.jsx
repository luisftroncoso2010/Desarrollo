import './App.css'
import  { Link } from "react-router-dom"
function App() { 

  return (
    <>
    <nav>
      
      <Link to="/home" > Home </Link>
      <Link to="/about" > About </Link>
      <Link to="/faqs" > Faqs </Link>
    </nav>
      
    </>
  )
}

export default App
