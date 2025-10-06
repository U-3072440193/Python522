import React from "react";
import './Main.css'
import MovieList from "../Components/MovieList";
import Preloader from "../Components/Preloader";
import Search from "../Components/Search";

class Main extends React.Component{
    state={
        movies:[]
    }
    componentDidMount(){
        fetch('http://www.omdbapi.com/?apikey=68c6159e&s=matrix').then(response => response.json())
        .then(data=> this.setState({movies:data.Search || []}))
    }

    searchMovie =(str)=>{
        fetch(`http://www.omdbapi.com/?apikey=68c6159e&s=${str}`).then(response => response.json())
        .then(data=> this.setState({movies:data.Search || []}))
    }

    render(){
        const {movies} = this.state
        return(
            <div className="main">
                <div className="wrap">
                    <Search searchMovie={this.searchMovie}/>
                    {movies.length ? <MovieList movies={movies}/> : <h3><Preloader/></h3>}
                    
                </div>
            </div>
        )
    }
}
export default Main;