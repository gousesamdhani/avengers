import React from "react";
import { Route, Redirect, HashRouter } from "react-router-dom";


export default ({ component: C, props: cProps, ...rest }) =>
  <Route
    {...rest}
    render={props =>
      cProps.isAuthenticated
        ? <HashRouter><C {...props} {...cProps} /></HashRouter>
        : <Redirect
            to={`/login?redirect=${props.location.pathname}${props.location.search}`}
          />}
  />;
