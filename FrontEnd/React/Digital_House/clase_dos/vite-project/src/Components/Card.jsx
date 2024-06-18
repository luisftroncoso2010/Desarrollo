import CardStyle from '../Styles/Card.module.css'
import PropTypes from 'prop-types'
import { Counter } from './Counter';

const Card = ({item, setCart}) => {   
    
  const { image, title, pricePerServing } = item 

  return (
    <div className={CardStyle.cardContainer}>        
        <img src={image} alt={title} className={CardStyle.cardImg}/>
        <h4>{title}</h4>
        <h4>${pricePerServing}</h4>
        <Counter />
        <button onClick={() => setCart((prevState) =>[...prevState, item])}>🛒</button>                            
    </div>
  )
}

export { Card }
