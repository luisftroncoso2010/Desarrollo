import CardStyle from '../Styles/Card.module.css'
import PropTypes from 'prop-types'
import { Counter } from './Counter';
import { Link } from 'react-router-dom';

const Card = ({item, setCart}) => {   
    
  const { image, title, pricePerServing } = item 

  return (
    <div className={CardStyle.cardContainer}>
        <Link to={'/detail/' + item.id}>
          <img src={image} alt={title} className={CardStyle.cardImg}/>
          <h4>{title}</h4>        
        </Link>        
        <h4>${pricePerServing}</h4>
        <Counter />
        <button onClick={() => setCart((prevState) =>[...prevState, item])}>🛒</button>                            
    </div>
  )
}

export { Card }
