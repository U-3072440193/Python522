import {useState} from "react";
function Item(){
    let [item,setItem] =useState([]);
    function addItem(){
        setItem(
            [
                ...item,
                Math.floor(Math.random()*10)+1
            ]
            ) 
    }
    return(
        <div>
            <button onClick={addItem}>Add a numb</button>
            {
                item.map((i,index)=>(<div key={index}
                style={{background: i % 2 ? 'gray': 'yellow'}}>{i}</div>))
            }
            
        </div>
    )
}
export default Item;