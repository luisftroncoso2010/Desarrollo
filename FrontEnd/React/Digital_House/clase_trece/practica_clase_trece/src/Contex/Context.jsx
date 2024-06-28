import { createContext, useContext, useState } from "react";

// Con esto se crea el contexto
export const RecipeState = createContext()

const Context = ({children}) => {

    const [salario, setSalario] = useState(10)
    const [ cart, setCart ] = useState([]) 

    return (
        <RecipeState.Provider value={{salario, setSalario}}>
          {children}         
        </RecipeState.Provider>
    )
}

export { Context }

// usamos el useConxtex y pasamos el contexto creado
export const useRecipeStates = () => {
    return useContext(RecipeState)
}