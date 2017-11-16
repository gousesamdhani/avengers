
import React, { Component } from "react";
import { FormGroup, FormControl, ControlLabel, Row, Col, Panel, Alert } from "react-bootstrap";
import Card from 'components/Card/Card';
import Button from 'elements/CustomButton/CustomButton.jsx';
import './login.css';

var api =  require('../utils/api');


export default class SignUp extends Component {

  constructor(props) {
    super(props);

    this.state = {
      email: "",
      username: "",
      password1: "",
      password2: "",
      message: "",
      subject: "",
      show_alert: false
    };
  }

  validateForm() {
    return this.state.email.length > 0 && this.state.password1.length > 0 && this.state.password2.length > 0;
  }

  handleChange = event => {
    this.setState({
      [event.target.id]: event.target.value
    });
  }

  handleSubmit = event => {
    var self = this;
    event.preventDefault();
    api.sign_up(this.state)
      .then(function (response) {
          if (response.success) {
                self.setState({
                  subject: "Successfully Registered!", 
                  message: "Please login to continue", 
                  alert_style: "success",
                  show_alert: true
                });
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
      <div className="container sign_up-container">
        <h2>Sign Up</h2>
        <Row>
        <Col sm={6} smOffset={3}>
        <form onSubmit={this.handleSubmit}> 
          <FormGroup controlId="username">
          <Row>
            <FormControl
              placeholder="Choose a username"
              value={this.state.username}
              onChange={this.handleChange}
            />
          </Row>
          </FormGroup>
          <FormGroup controlId="email">
          <Row>
            <FormControl
              type="email"
              placeholder="Email"
              value={this.state.email}
              onChange={this.handleChange}
            />
          </Row>
          </FormGroup>
          <FormGroup controlId="password1">
          <Row>
            <FormControl
              type="password"
              placeholder="Password"
              value={this.state.password1}
              onChange={this.handleChange}
            />
          </Row>
          </FormGroup>
          <FormGroup controlId="password2">
          <Row>
            <FormControl
              type="password"
              placeholder="Re-enter Password"
              value={this.state.password2}
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
            Sign Up
          </Button>
          </Col>
          <Col sm={4} smOffset={4}>
          <Button
            block
            bsStyle="link"
            bsSize="sm"
            href="/login"
          >
          Already a member? Sign in
          </Button>
          </Col>
          </Row>
          {
            this.state.show_alert && (<Alert bsStyle={this.state.alert_style} bsSize="sm">
              <strong>{this.state.subject}</strong> {this.state.message}
            </Alert>)
          }
        </form>
        </Col>
        </Row>
      </div>
      </div>
    );
  }

}
