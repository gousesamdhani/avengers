import React, { Component } from 'react';
import Routes from "./Routes";


class Main extends Component {

	constructor(props) {
	  super(props);

	  this.state = {
	    isAuthenticated: false
	  };
	}

	componentDidMount() {
	  try {
	  	var token = localStorage.getItem('avengers_secret');
	    if (token) {
	      this.userHasAuthenticated(true);
	    }
	  }
	  catch(e) {
	    alert(e);
	  }
	}


	userHasAuthenticated = authenticated => {
	  this.setState({ isAuthenticated: authenticated });
	}

	render() {
		const childProps = {
  			isAuthenticated: this.state.isAuthenticated,
  			userHasAuthenticated: this.userHasAuthenticated
		};
	    return (
	      <div className="App">
	        <Routes childProps={childProps} />
	      </div>
	    );
	}

}

export default Main;
