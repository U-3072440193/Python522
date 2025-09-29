
import './App.css';
import Header from './Header.js'


function App(props) {

let {title, slogan, logo} = props;
  return (
    <div className="App">
      <Header title={title} slogan={slogan} logo ={logo} />

    </div>
  );
}

export default App;
