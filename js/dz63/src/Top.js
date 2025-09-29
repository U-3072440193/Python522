import './Top.css'


function Top(props){
    let {db, poster} = props;
    
    return(
        <div className="app">
            {Object.keys(db).map((elem, index) => {
                return(
                    <div className="card" key={index}>
                        <img src={poster[index]} alt={db[elem].title} />
                        <div className="title">{db[elem].title}</div>
                        <div className="genre">{db[elem].genre}</div>
                        <div className="rating">{db[elem].rating}</div>
                        <div className="country-director">{db[elem].director}, {db[elem].country}</div>
                        <div className="year">{db[elem].year}</div>
                    </div>
                )
            })}
        </div>
    )
};
export default Top;