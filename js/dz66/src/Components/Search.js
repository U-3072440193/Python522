import React from "react";
import './Search.css';

class Search extends React.Component {
    state = {
        search: "",
        type: "all",
        page: 1
    }

    handleKey = (event) => {
        if (event.key === 'Enter') {
            this.props.searchMovie(this.state.search, this.state.type, this.state.page)
        }
    }

    handelFilter = (event) => {
        this.setState(
            () => ({ type: event.target.dataset.type }),
            () => { this.props.searchMovie(this.state.search, this.state.type, this.state.page) }
        );
    }

    prevPage = () => {
        this.setState(
            this.state.page > 1 ? { page: this.state.page - 1 } : { page: 1 },
            () => { this.props.searchMovie(this.state.search, this.state.type, this.state.page) }
        )
    }

    nextPage = () => {
        this.setState(
            { page: this.state.page + 1 },
            () => { this.props.searchMovie(this.state.search, this.state.type, this.state.page) }
        )
    }
    maxPage = () => {
    const result = Math.floor((this.props.totalResults - 1) / 10) + 1;
    console.log('maxPage:', result, 'totalResults:', this.props.totalResults);
    return result;
}
    
    changePage = (num) => {
        console.log(this.props.totalResults);
        const newPage = this.state.page + num;
        if (newPage < 1 || newPage > this.maxPage()) return; 
        this.setState(
            { page: newPage },
            () => { this.props.searchMovie(this.state.search, this.state.type, this.state.page) }
        )
    }
    

    render() {
        
        return (
            <>
                <div className="search">
                    <input
                        type="search"
                        placeholder="Search"
                        value={this.state.search}
                        onChange={(e) => this.setState({ search: e.target.value })}
                        onKeyDown={this.handleKey}
                    />
                    <button
                        className="btn"
                        onClick={() => {this.setState({ page: 1 });this.props.searchMovie(this.state.search, this.state.type, this.state.page)}}
                    >Search</button>
                </div>
                <div className="radio">
                    <input type="radio" name="type" data-type="all" checked={this.state.type === 'all'} onChange={this.handelFilter} id="all" /> <label htmlFor="all">All</label>
                    <input type="radio" name="type" data-type="movie" checked={this.state.type === 'movie'} onChange={this.handelFilter} id="movies" /> <label htmlFor="movies">Movies</label>
                    <input type="radio" name="type" data-type="series" checked={this.state.type === 'series'} onChange={this.handelFilter} id="series" /> <label htmlFor="series">Series</label>
                    <input type="radio" name="type" data-type="game" checked={this.state.type === 'game'} onChange={this.handelFilter} id="games" /> <label htmlFor="games">Games</label>
                </div>
                <div className="butt-container" >
                    <div className="navigation">
                    <button className="btn butt" onClick={this.prevPage}>Prev</button>
                </div>
                <div className="scrollContainer">
                    <button className={`btn ${this.state.page - 2 < 1 ? 'hidden' : ''}`}onClick={()=>(this.changePage(-2))}>{this.state.page - 2}</button>
                    <button className={`btn ${this.state.page - 1 < 1 ? 'hidden' : ''}`} onClick={()=>(this.changePage(-1))}>{this.state.page - 1}</button>
                    <button className="btn view">{this.state.page}</button>
                    <button className={`btn ${this.state.page + 1 > this.maxPage() ? 'hidden' : ''}`}onClick={()=>(this.changePage(1))}>{this.state.page + 1}</button>
                    <button className={`btn ${this.state.page + 2 > this.maxPage() ? 'hidden' : ''}`}onClick={()=>(this.changePage(2))}>{this.state.page + 2}</button>
                </div>
                <div className="navigation"> 
                    <button className="btn butt" onClick={this.nextPage}>Next</button>
                </div>


                </div>


                <div className="totalResults">
                    <div>Найдено: {this.props.totalResults} </div>
                </div>
                
            </>
        )
    }
}

export default Search;