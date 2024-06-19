import React from 'react'
import { useNavigate } from 'react-router-dom'

const Home = () => {
    const navigate = useNavigate()

  return (
    <div>
      Estas en el Home
      <br />
      <button onClick={() => navigate(-1)}> Go back</button>
    </div>
  )
}

export default Home
