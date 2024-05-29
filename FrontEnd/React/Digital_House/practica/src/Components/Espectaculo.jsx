const Espectaculo = ({item, setShowForm}) => {
    return (
        <div>
            <img src={item.img} alt=""/>
            <h3>{item.artista}</h3>
            <h3>Entradas desde: ${item.precio}</h3>
            <button onClick={() => setShowForm(true)}>Comprar entradas</button>
        </div>
    )
}

export { Espectaculo }