import React from "react";
import './Search.css'

class Search extends React.Component{
    state = {
        search: ""
    }
    

    render() {
        const {searchMovie} = this.props
        return (
            <div className="search">
                <input
                    type="search"
                    placeholder="Search"
                    value={this.state.search}
                    onChange={(e) => {this.setState({ search: e.target.value });searchMovie(e.target.value);
                        }}
                />  
            </div>
        ) 
    }
}

export default Search;