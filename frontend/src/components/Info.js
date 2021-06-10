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
             <img src={'/static/'+this.props.e.fotos[0].file} />
          <div>{this.props.e.descripción}</div>
          <div>Likes: {this.props.e.likes}</div>
          <Button variant="primary" onClick={() => this.props.handleInfo()}>Atrás</Button>
        </Container>
	)}
}

export default Info