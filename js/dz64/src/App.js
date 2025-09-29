import './App.css';
import React from 'react';
import Range from './Range' 


class App extends React.Component {
  state = {
    posts: [
      {id:'1',name:'js base', title:'learn some'},
      {id:'2',name:'js adv', title:'learn some more'},
      {id:'3',name:'react', title:'learn all'}
    ]
  }
  render() {
    return (
      <div >
        <Range /> 
      </div>
    );
  }
}

export default App;