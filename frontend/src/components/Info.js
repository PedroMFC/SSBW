import React from 'react';
import Container from 'react-bootstrap/esm/Container';
import Button from 'react-bootstrap/Button'

class Info extends React.Component {

	constructor(props) {
		super(props)
	}
	

	// onChange bindeada para que coja el this
	render() {
		return (  
        <Container>
        <h1>
          {this.props.e.nombre}
        </h1>
             <img
            src={'../logo-senderos.gif'}

          />
          <div>{this.props.e.descripción}</div>
          <Button variant="primary" onClick={() => this.props.handleInfo()}>Atrás</Button>
        </Container>
	)}
}

export default Info