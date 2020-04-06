import React from 'react';
import { Switch, Route } from 'react-router-dom';
import AuthenticatedRoute from '../components/AuthenticatedRoute';
import UnauthenticatedRoute from '../components/UnAuthenticatedRoute';
import SignIn from '../containers/Signin';
import SignUp from '../containers/Signup';
import NotFound from '../containers/NotFound';
import DashBoard from '../containers/DashBoard';

function Routes({ appProps }){
    return (
        <Switch>
            <UnauthenticatedRoute exact path='/login' appProps={appProps} component={SignIn} />
            <Route exact path='/register' component={SignUp} />
            <AuthenticatedRoute exact path='/dashboard' appProps={appProps} component={DashBoard} />
            <Route component={NotFound} />
        </Switch>
    )
}

export default Routes;