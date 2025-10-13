import {useState} from "react";

function Counter(){
    let [cnt,setCnt]= useState(0);
    let increment =() => setCnt(cnt+1);
    let decrement =() => setCnt(cnt-1);
    return(
        <div>
                <h2>Counter</h2>
                <h1>{cnt}</h1>
                <button onClick={decrement}>- Minus</button>
                <button onClick={increment}>+ Plus</button>
        </div>
    )
}
export default Counter;