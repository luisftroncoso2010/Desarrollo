import CardStyle from '../Styles/Card.module.css'
console.log(CardStyle);
import PropTypes from 'prop-types'


const Card = (props) => {
    const { pizza } = props    

  return (
    <div className={CardStyle.cardContainer}>        
        <img src={pizza.img} alt={pizza.tipo} className={CardStyle.cardImg}/>
        <h4>{pizza.tipo}</h4>
        <h4>${pizza.precio}</h4>
        <button>🛒</button>                            
    </div>
  )
}

Card.propTypes = {
    pizza: PropTypes.shape({
      img: PropTypes.string.isRequired,
      tipo: PropTypes.string.isRequired,
      precio: PropTypes.string.isRequired,
    }).isRequired,
  }

export {Card}
