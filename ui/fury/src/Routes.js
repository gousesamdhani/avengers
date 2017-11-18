
import React from "react";
import AuthenticatedRoute from "./components/AuthenticatedRoute";
import UnauthenticatedRoute from "./components/UnauthenticatedRoute";
import { Route, Switch } from "react-router-dom";
import Login from "./containers/Login";
import SignUp from "./containers/SignUp";
import App from "./containers/App/App";


export default ({ childProps }) =>
  <Switch>
    <UnauthenticatedRoute path="/" exact component={Login} props={childProps} />
    <UnauthenticatedRoute path="/login" exact component={Login} props={childProps} />
    <UnauthenticatedRoute path="/signup" exact component={SignUp} props={childProps} />
    <AuthenticatedRoute path="/app" exact component={App} props={childProps} />
  </Switch>;