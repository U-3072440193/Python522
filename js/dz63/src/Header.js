import logo from './logo.svg';
import './Header.css'
function Header(props){
    let {title, slogan} = props;
    return (
        
        <header className="App-header">
            <img src={logo} className="App-logo" alt="logo" />
            <p>
            Edit <code>src/App.js</code> and save to reload.
            </p>
            <h1>{title}</h1>
            <p>{slogan}</p>
      </header>
    )
}
export default Header;