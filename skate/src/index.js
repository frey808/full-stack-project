import React from 'react';
import ReactDOM from 'react-dom/client';
import './index.css';
import Skate from './skate';
import reportWebVitals from './reportWebVitals';

const root = ReactDOM.createRoot(document.getElementById('root'));
root.render(
  <React.StrictMode>
    <Skate/>
  </React.StrictMode>
);

reportWebVitals();
