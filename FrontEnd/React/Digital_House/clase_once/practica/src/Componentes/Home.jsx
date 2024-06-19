import React from 'react'
import { useNavigate } from 'react-router-dom'

const Home = () => {
    const navigate = useNavigate()

    const handleClick = () => {
        navigate(-1)
      }

  return (
    <div>
      Estas en el Home
      <br />
      <button onClick={handleClick}> Go back, App</button>
    </div>
  )
}

export default Home
