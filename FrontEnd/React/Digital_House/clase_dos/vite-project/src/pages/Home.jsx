import { useEffect, useState } from "react";
import { Card } from "../Components/Card"
import axios from 'axios';


const titleStyle = {
  backgroundColor: '#ffda92',
  color: 'firebrick',
  width: '20%',
  margin: '10px auto',
  borderRadius: '10px',
}

let pizzas = [
  { id: 1, tipo: 'Muzzarella', precio: '1200', img: 'https://www.johaprato.com/files/styles/flexslider_full/public/pizza_de_mozzarella.jpg?itok=0X9_f7K8' },
  { id: 2, tipo: 'Fugazza', precio: '1250', img: 'https://cdn0.recetasgratis.net/es/posts/7/0/2/pizza_fugazza_7207_600.webp' },
  { id: 3, tipo: 'Napolitana', precio: '1350', img: 'https://img-global.cpcdn.com/recipes/5fb5d55852fa8d06/640x640sq70/photo.webp' },
  { id: 4, tipo: 'Rucula y crudo', precio: '1500', img: 'https://pizzasargentinas.com/wp-content/uploads/2020/12/rucula-y-jamon-crudo.jpg' },
  { id: 5, tipo: 'Especial', precio: '1400', img: 'https://saboresmendoza.com/wp-content/uploads/2024/02/pizza-3.jpg' },
] 
const Home = () => { 
  const [cart, setCart] = useState([])
  const [recipes, setRecipes] = useState([])
  const apiKey = '68d481a0fbc340308fbf934f836ee8c6'
  const url = 'https://api.spoonacular.com/recipes/random?number=10&apiKey='+ apiKey

  useEffect(() => {
    axios(url).then((result) => setRecipes(result.data.recipes))
  }, [])  
  
  console.log(recipes);
  
  return (
    <div>
      <h2>Pizzas seleccionadas</h2>
      <ul>
       { cart.map((pedido) => <li key={pedido.id}>{pedido.title}</li>) }
      </ul>      
      <h1 style={titleStyle}>Lista de Recetas</h1>
        <div className="list-container">
          {recipes.map((recipe) => <Card item={recipe} key={recipe.id} setCart={setCart} />)}       
        </div>      
    </div>
  )
}

export  { Home }
