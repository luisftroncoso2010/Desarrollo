const Envio = ( {cliente} ) => {
    const {nombre, direccion} = cliente
  return (
    <>
      <h3>Nombre: {nombre} </h3>
      <h3>Direccion: {direccion} </h3>     
    </>
  )
}

export { Envio }
