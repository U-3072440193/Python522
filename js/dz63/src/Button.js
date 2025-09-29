import './index.css'

function Button(props){
    let {torrent} = props
    return(
        <div className="button-container">
            <a href="http://localhost:3000/#" className='buttonOne'>
                {torrent}
            </a>
        </div>
    )
}
export default Button;