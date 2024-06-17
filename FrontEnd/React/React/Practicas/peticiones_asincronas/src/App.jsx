import { useCallback, useState } from 'react'
import './App.css'
import { Peticiones } from './Components/Peticiones'
import { Todos } from './Components/Todos'
import { ExampleFetch } from './Components/ExampleFetch'
import { AsyncAwait } from './Components/AsyncAwait'


function App() {
  const [count, setCount] = useState(0)
  const [todos, setTodos] = useState([])

  const increment = () => {
    return setCount((c) => c + 1)    
  }



  const addTodo = useCallback(() => {
    setTodos((t) => [...t, "New Todo"])
  }, [todos])

  return (
    <>
     <Todos todos={todos} addTodo={addTodo} />
     <hr />
     <div>
      Count: {count}
      <br />
      <button onClick={increment}>+</button>
     </div>
     <Peticiones/>
     <ExampleFetch/>
     <AsyncAwait />
    </>
  )
}

export default App
