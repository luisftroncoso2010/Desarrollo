import CardStyle from '../Styles/Card.module.css'
import PropTypes from 'prop-types'
import { Counter } from './Counter';

const Card = ({item, setCart}) => {   
    
  const { img, tipo, precio } = item 

  return (
    <div className={CardStyle.cardContainer}>        
        <img src={img} alt={tipo} className={CardStyle.cardImg}/>
        <h4>{tipo}</h4>
        <h4>${precio}</h4>
        <Counter />
        <button onClick={() => setCart((prevState) =>[...prevState, item])}>🛒</button>                            
    </div>
  )
}

Card.propTypes = {
    item: PropTypes.shape({
      img: PropTypes.string.isRequired,
      tipo: PropTypes.string.isRequired,
      precio: PropTypes.string.isRequired,      
    }).isRequired,       
    setCart: PropTypes.func.isRequired,      
  }

export { Card }
