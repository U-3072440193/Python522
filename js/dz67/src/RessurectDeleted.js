import { useState } from 'react';
function RessurectDeleted(props) { 
    let { deletedTasks,ressurectTask } = props;
    let [isVisible, setIsVisible] = useState(false);

    
    return(
        <div>
            <button onClick={() => setIsVisible(true)}>Показать</button>
            <button onClick={() => setIsVisible(false)}>Убрать</button>
            <div style={{display: isVisible===true ? 'block' : 'none' }}>
                {deletedTasks.map((task, index) => (
                    <div className="task" key={index}>
                        {task.text}
                        <button onClick={()=>{ressurectTask(index)}}>Вернуть назад</button>
                    </div>
                ))}
            </div>
        </div>

    )
}
export default RessurectDeleted;