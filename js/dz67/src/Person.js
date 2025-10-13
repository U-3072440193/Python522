import {useState} from "react";

function Person(){
    let [person, setPerson]=useState({
        'firstName': 'Igor',
        "lastName":'Petro'
    });
    function rename(){setPerson({...person,firstName:'Sirgay'})}

    return(
        <div>
            <p>{person.firstName} {person.lastName}</p>
            <button onClick={rename}>Rename</button>
        </div>
    )
}
export default Person;