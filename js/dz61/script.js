/* fetch('https://jsonplaceholder.typicode.com/todos')
      .then(response => response.json())
      .then(js => console.log(js)) */

document.querySelector("#load").addEventListener("click",loadUsers);

function loadUsers(){
    let url = "https://jsonplaceholder.typicode.com/todos"
    fetch(url)
    .then(function (response){
        return response.json()
    })
    .then(function (data){
        let ul = document.querySelector("#list");
        let html = data.map(function(item){
            if(item.completed == true){
                return "<li> Пользователь"+ item.userId + " Выполниз задачу №" + item.id + " (" + item.title +")"+ "</li>";
            }

        })
        ul.insertAdjacentHTML('afterbegin',html.join(" "));
    })
}