import React from "react";

class Range extends React.Component{
    state = {
        width: 100,
        height: 150
    }

    range = (event) => {
        this.setState({
            [event.target.name]: event.target.value
        })
    }
    
    render(){
        return(
            <>
                <input name="width" type="range" onChange={this.range} min="0" max="255" step="0.1" />
                <p>Ширина: {this.state.width}</p>
                
                <input name="height" type="range" onChange={this.range} min="0" max="255" step="0.1" />
                <p>Высота: {this.state.height}</p>

                <input name="b" type="range" onChange={this.range} min="0" max="255" step="0.1" />
                <p>б дла РГБ: {this.state.b}</p>
                
                <div style={{ 
                    width: `${this.state.width}px`, 
                    height: `${this.state.height}px`, 
                    backgroundColor: `rgb(${this.state.width}, ${this.state.height}, ${this.state.b})` 
                }}></div>
            </>
        )
    }
}
export default Range;