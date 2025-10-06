import './Movie.css'

function Movie(props){
    const {Title,Year,imdbID,Type,Poster} = props;
    return(
<div className="card">
  <img src={Poster} alt={imdbID} />
  <h3>{Title}</h3>
  <div className="card-info">
    <p>{Year}</p>
    <p>{Type}</p>
  </div>
</div>
    )
}

export default Movie;