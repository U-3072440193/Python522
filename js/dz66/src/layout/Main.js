import React from "react";
import './Main.css'
import MovieList from "../Components/MovieList";
import Preloader from "../Components/Preloader";
import Search from "../Components/Search";

class Main extends React.Component{
    state={
        movies:[],
        loading: true,
        totalResults:1
    }
    componentDidMount(){
        fetch('http://www.omdbapi.com/?apikey=68c6159e&s=matrix').then(response => response.json())
        .then(data=> this.setState({movies:data.Search, loading: false,totalResults:data.totalResults || 1}))
    }

    searchMovie =(str,type='all',page,totalResults=1)=>{
        this.setState({loading:true})
        fetch(`http://www.omdbapi.com/?apikey=68c6159e&s=${str}${type !== 'all' ? `&type=${type}` :''}${`&page=${page}`}`)
        .then(response => response.json())
        .then(data => this.setState({ movies: data.Search, loading: false,totalResults:data.totalResults ||1 }))
    }

    render(){
        const {movies,loading,totalResults} = this.state
        return(
            <div className="main">
                <div className="wrap">
                    <Search searchMovie ={this.searchMovie} totalResults={totalResults}/>
                    {loading ? <Preloader/> : <MovieList movies={movies}/> }
                    
                </div>
            </div>
        )
    }
}
export default Main;