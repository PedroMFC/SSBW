import logo from './logo-senderos.gif';
import Container from 'react-bootstrap/Container'
import Navbar from 'react-bootstrap/Navbar'
import './App.css';
import React from 'react';

class App extends React.Component {
  constructor(props) {
    super(props)

  	this.state = {
    	excursiones:[],
		}
	}

  componentDidMount() {
		const url = 'http://localhost:8000/api/excursiones'

		// una promise, que devuelve otra promise
		fetch(url)
			.then(res => res.json())
			.then(res => {
						console.log(res)
						this.setState({excursiones:res})   // Se cambia el state y re-renderiza
					})
			.catch(error => {
				alert('Error '+ error)
			})
	}

  render() {
    return (
      <Container fluid>
        <Navbar bg="light">
          <img
            alt = ""
            src={logo}
            width = "40"
            height = "40"
            className="d-inline-block-align-top"
          />{' '}
          <span style={{marginLeft:'2vw'}}>Senderos Granada</span>
        </Navbar>
      </Container>
    );
  }

}

export default App;
