import logo from './logo-senderos.gif';
import Container from 'react-bootstrap/Container'
import Navbar from 'react-bootstrap/Navbar'
import './App.css';
import React from 'react';
import Busqueda from './components/Busqueda.js';
import Info from './components/Info.js';
import ExcursionesList from './components/ExcursionesList.js';

class App extends React.Component {
  constructor(props) {
    super(props)

  	this.state = {
    	excursiones:[],
      informacion: '',
      busqueda: ''
		}
	}

  componentDidMount() {
		const url = 'http://localhost:8000/api/excursiones'

		// una promise, que devuelve otra promise
		fetch(url)
			.then(res => res.json())
			.then(res => {
						let excursion = res.map( e=> {
              e.on = true
              return e
            })
            console.log(excursion)
						this.setState({excursiones:excursion})   
					})
			.catch(error => {
				alert('Error '+ error)
			})
	}

  infoID = () => {
    const [e] = this.state.excursiones.filter(e => e.id == this.state.info)
    return e
  }

  excursiones = () =>{
    return this.state.excursiones.filter( e => e.on == true)
  }

  handleInfo = (id) =>{
    if (id === ''){
      this.setState({info: ''})
    } else{
      this.setState({info:id})
    }
  }

  handleBuscar = (term) =>{
    if (term){
      let excursion = this.state.excursiones.map( e =>{
        let expr = new RegExp(term, "i")
        console.log('Expr ', expr)
        if(!e.nombre.match(expr) && !e.descripción.match(expr)){
          e.on = false
        } else{
          e.on = true
        }
        return e
      })
      this.setState({excursiones:excursion})
    } else{
      let excursion = this.state.excursiones.map( e =>{
        e.on = true
        return e
      })
      this.setState({excursiones:excursion})
    }
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
        <Container>
          { this.state.info ? <Info e={this.infoID()} handleInfo = {this.handleInfo} />:
          <>
          <Busqueda handleBuscar={this.handleBuscar}/>
          <ExcursionesList excursiones = {this.excursiones()}
                          handleInfo = {this.handleInfo}/>
          </>   
        }
        </Container>
      </Container>
    );
  }

}

export default App;
