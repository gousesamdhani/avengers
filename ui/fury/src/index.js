import React from 'react';
import ReactDOM from 'react-dom';
import Main from 'Main';

import {
    BrowserRouter,
    Route,
    Switch
} from 'react-router-dom';


import './assets/css/bootstrap.min.css';
import './assets/css/animate.min.css';
import './assets/sass/light-bootstrap-dashboard.css';
import './assets/css/demo.css';
import './assets/css/pe-icon-7-stroke.css';




ReactDOM.render((
    <BrowserRouter>
        <Main />
    </BrowserRouter>
),document.getElementById('root'));
