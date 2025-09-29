
import './Header.css'

function Header(props){
    let {title, slogan,logo} = props;
    return (
        
        <header className="App-header">
            <img src={logo} alt="logo" />
        
            <h1>{title}</h1>
            <p>{slogan}</p>
      </header>
    )
}
export default Header;