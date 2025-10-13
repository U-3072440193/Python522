import { useState } from "react";

function Form(props) { 
    let [value, setValue] = useState('');
    let { addTask } = props;
    
    let handleSubmit = e => { 
        e.preventDefault();
        addTask(value);
        setValue(''); 
    }
    
    return(
        <div>
            <form onSubmit={handleSubmit}> 
                <input 
                    type="text" 
                    className="input" 
                    value={value}
                    onChange={e => setValue(e.target.value)}
                    placeholder="Добавить новую задачу"
                />
                <button type="submit">Добавить</button>
                
            </form>
        
        </div>
    )
}

export default Form;