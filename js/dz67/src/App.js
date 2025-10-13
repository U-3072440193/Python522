import './App.css';
import { useState } from 'react';
// import Counter from './Counter';
// import Person from './Person';
// import Modal from './Modal';
// import Item from './Item';
import Task from './Task';
import Form from './Form';
import RessurectDeleted from './RessurectDeleted';
import CountTask from './CountTask';
 
function App() {
 
  let [tasks, setTasks] = useState([
    {
      text: "Выучить JavaScript",
      done: false
    },
    {
      text: "Познакомиться с React",
      done: false
    },
    {
      text: "Устроиться на работу",
      done: false
    }
  ])
  let [deletedTasks, setDeletedTasks] = useState([]) 
 
 
  let addTask = text => {
    let newTask = [...tasks, { text }];
    setTasks(newTask);
  }
  let deleteTask = index =>{ //Удаление элем из главного массива+сохранение удаленного
    let newTask = [...tasks];
    let deletedEl = newTask.splice(index,1)[0]; 
    setTasks(newTask);
    setDeletedTasks([...deletedTasks, deletedEl]);

  }
 
  let doneTask = index => {
    let newTask = [...tasks];
    newTask[index].done = true;
    setTasks(newTask);
  }
let ressurectTask = index => { //Массив для удаленных тасков
    
    let taskToRestore = deletedTasks[index];
    
    let newDeletedTasks = [...deletedTasks];
    newDeletedTasks.splice(index, 1);
    setTasks([...tasks, taskToRestore]);
    setDeletedTasks(newDeletedTasks);
}
 
  return (
 
 
    <div className="App">
      <div className='task-list'>
        {
          console.log(tasks)
        }
        {/* <Counter />
      <Person />
      <Modal />
      <Item />*/}
        {
          tasks.map((task, index) =>
            <Task
              key={index}
              task={task}
              doneTask={doneTask}
              index={index}
              deleteTask={deleteTask}
              ressurectTask={ressurectTask}
              deletedTasks={deletedTasks}

            />
          )
        }
        <Form addTask={addTask}/>
        <RessurectDeleted
          ressurectTask={ressurectTask}
          deletedTasks={deletedTasks}
        />
        <CountTask 
        tasks={tasks}
        />
      </div>
    </div>
  );
}
 
export default App;