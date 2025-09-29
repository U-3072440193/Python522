import React from"react";

class Footer extends React.Component{
    render(){
        let {text} = this.props;
        return(
            <footer style={{background: "#a32b2bff"}}>
                <p>{text}</p>
            </footer>
        )
    }
}
export default Footer;