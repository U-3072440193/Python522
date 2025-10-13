//import { useState } from 'react';
function CountTask(props) { 
    let {tasks} = props

let doneOnes = () => {
    let count = 0;
    
    tasks.map(task => {
        if (task.done) {
            count++;
        }
        return task; 
    });
    
    return count;
}
    return(
        <div>
            Количество задач {tasks.length}, сделано {doneOnes()}
        </div>

    )
}
export default CountTask;