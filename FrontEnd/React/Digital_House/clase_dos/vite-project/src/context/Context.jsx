import { createContext, useContext, useState, useEffect } from "react"
import axios from 'axios';

// Creamos contexto
const RecipeStates = createContext()

const Context = ({ children }) => {

  const [cart, setCart] = useState([])
  const [recipes, setRecipes] = useState([])
  const apiKey = '68d481a0fbc340308fbf934f836ee8c6'
  const url = 'https://api.spoonacular.com/recipes/random?number=10&apiKey='+ apiKey

  useEffect(() => {
    axios(url).then((result) => setRecipes(result.data.recipes))
    .catch((err) => console.log(err))
  }, [])    
     
    return(
        <RecipeStates.Provider
         value={{cart, setCart, recipes}} >
         {children}
        </RecipeStates.Provider>
    )
}

export { Context }

export const useRecipesStates = () => {
    return useContext(RecipeStates)
}