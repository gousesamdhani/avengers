
import React, { Component } from "react";
import Button from 'elements/CustomButton/CustomButton.jsx';
import { FormGroup, FormControl, ControlLabel, Row, Col, Panel, Alert } from "react-bootstrap";
import './login.css';
var api =  require('../utils/api');



export default class Login extends Component {

  constructor(props) {
    super(props);

    this.state = {
      username: "",
      password: "",
      message: "",
      subject: "",
      show_alert: false
    };
  }

  validateForm() {
    return this.state.username.length > 0 && this.state.password.length > 0;
  }

  handleChange = event => {
    this.setState({
      [event.target.id]: event.target.value
    });
  }

  handleSubmit = event => {
    var self = this;
    event.preventDefault();
    api.login(this.state)
      .then(function (response) {
          if (response.success) {
                var token = response.data.key;
                localStorage.setItem('avengers_secret', token);
                self.setState({
                  subject: "Login Successfull!", 
                  alert_style: "success",
                  show_alert: true
                });
                self.props.userHasAuthenticated(true);
                self.props.history.push("/app");
          } else {
                self.setState({
                  subject: "", 
                  message: self.get_form_errors(response),
                  alert_style: "warning",
                  show_alert: true
                });
          }
    })
  }

  get_form_errors (response) {

    var errors = "";
    for(var key in response) {
      if(key == 'success')
        continue;
      errors += response[key].join(' . ');
    }
    return errors;
  }


  render() {
    return (
      <div>
      <div className="container login-container">
        <h2>Sign in</h2>
        <Row>
        <Col sm={6} smOffset={3}>
        <form onSubmit={this.handleSubmit}>
          <FormGroup controlId="username">
          <Row>
            <FormControl
              autoFocus
              type="username"
              placeholder="Username"
              value={this.state.username}
              onChange={this.handleChange}
            />
          </Row>
          </FormGroup>
          <FormGroup controlId="password">
          <Row>
            <FormControl
              type="password"
              placeholder="Password"
              value={this.state.password}
              onChange={this.handleChange}
            />
          </Row>
          </FormGroup>
          <Row>
          <Col sm={4} smOffset={4}>
          <Button
            block
            bsStyle="info"
            fill
            bsSize="medium"
            disabled={!this.validateForm()}
            type="submit"
          >
            Login
          </Button>
          </Col>
          <Col sm={4} smOffset={4}>
          <Button
            block
            bsStyle="link"
            bsSize="sm"
          >
            Forgot Password?
          </Button>
          </Col>
          <Col sm={4} smOffset={4}>
          <Button
            block
            bsStyle="link"
            bsSize="sm"
            href="/signup"
          >
          Not a member yet? SignUp
          </Button>
          </Col>
          </Row>
        </form>
        {
            this.state.show_alert && (<Alert bsStyle={this.state.alert_style} bsSize="sm">
              <strong>{this.state.subject}</strong> {this.state.message}
            </Alert>)
        }
        </Col>
        </Row>
      </div>
      </div>
    );
  }

}
