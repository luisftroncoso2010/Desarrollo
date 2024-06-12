import React, { Component } from 'react'

export default class ClassComponent extends Component {
    constructor(props){
        super(props)
        this.state = {
            nombre: ' ' 
        }
        console.log("Constructor Class Component");
    }

    componentDidMount(){
        console.log("Se renderizo el Class Component");
    }

    componentDidUpdate(){
        /* La actulizacion del componente no lo muestra */
        console.log("Se actulizó el Class Compoonent");

    }

    componentWillUnmount(){
        console.log("Se desmonta el Class Component");

    }

  render() {
    console.log("Render Class Component");
    return (
      <div>
        Class Component
      </div>
    )
  }
}
