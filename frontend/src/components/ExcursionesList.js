import React from 'react';
import ExcursionItem from "./ExcursionItem.js"
import Container from 'react-bootstrap/Container'

class ExcursionesList extends React.Component {

	constructor(props) {
		super(props)
	}
	

	// onChange bindeada para que coja el this
	render() {
		return (  
        <Container>
            {this.props.excursiones.map( excur =>(
                <ExcursionItem
                    key={excur.id}
                    id={excur.id}
                    nombre={excur.nombre}
                    descripción={excur.descripción}
                    img={excur.fotos[0].file}
                    handleInfo={this.props.handleInfo}
                />
            ))}
         </Container>
	)}
}

export default ExcursionesList