import React from 'react';
import ReactDOM from 'react-dom/client';
import './index.css';
import App from './App';
import data from './db.json';

let nav = {"Main": "/index","news":"/news", "about": "/about", "store": "/shop","contact": "/contacts"};
let text = "7mi site";
let slogan = "i banging react";
let db = data.people;
let icon = data.people.pol;
let copy = "Copyright - 2025";

const root = ReactDOM.createRoot(document.getElementById('root'));
root.render(
  <React.StrictMode>
    <App title={text} slogan={slogan} navigation={nav} db={db} icon={icon} copy={copy}/>
    
  </React.StrictMode>
);
