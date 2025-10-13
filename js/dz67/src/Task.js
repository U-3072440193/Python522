
import { useState } from 'react';
function Task(props){
    let {task,doneTask,index,deleteTask} = props;
    let [visLine, setVisLine] = useState(true); //Для отмены зачеркнутого текста
    return(
    <div>
        <div className="task">
            <span style={{textDecoration: task.done && visLine ? 'line-through' : 'none'}}>
                {task.text}
            </span>
            <div>
                <button onClick={() => {
                    doneTask(index);
                    setVisLine(!visLine);
                }}>done</button>
                <button onClick={()=> deleteTask(index)}>Х</button>
            </div>
        </div>
        
    </div>

    )
    
}
export default Task;