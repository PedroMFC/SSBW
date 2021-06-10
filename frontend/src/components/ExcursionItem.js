import React from 'react';
import Card from 'react-bootstrap/Card'
import Button from 'react-bootstrap/Button'

class ExcursionItem extends React.Component {

	constructor(props) {
		super(props)
	}
	

	// onChange bindeada para que coja el this
	render() {
        //const { img } = this.props

		return (  
            <Card style={{ width: '18rem' }}>
            <Card.Img src={'/static/'+this.props.img} />
            <Card.Body>
                <Card.Title>{this.props.nombre}</Card.Title>
                <Card.Text>
                {this.props.descripción}
                </Card.Text>
                <Button variant="primary" onClick={() => this.props.handleInfo(this.props.id)}>Información</Button>
            </Card.Body>
            </Card>
	)}
}

export default ExcursionItem