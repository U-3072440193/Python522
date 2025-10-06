import Movie from './Movie';
import './MovieList.css';

function MovieList(props) {
  const { movies = [] } = props;
  
  return (
    <div className="cards-container">
      {movies.map(movie => (
        <Movie {...movie} key={movie.imdbID} />
      ))}
    </div>
  );
}

export default MovieList;