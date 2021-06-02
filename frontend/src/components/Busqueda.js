import React from 'react';
import Form from 'react-bootstrap/Form'

class Busqueda extends React.Component {

	constructor(props) {
		super(props)
	}
	
	handleChange(event) {
        
        
		this.props.handleBuscar(event.target.value) // Pasar hacia arriba el valor
    }

	// onChange bindeada para que coja el this
	render() {
		return (  
			<Form style={{marginTop:'8%', paddingBottom:'2%'}}>
				<Form.Group>
					<Form.Label>Buscar excursiones</Form.Label>  
					<Form.Control type="text" placeholder="..." onChange={this.handleChange.bind(this)}/>
				</Form.Group>
			</Form>
	)}
}


export default Busqueda