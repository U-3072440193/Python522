let reg = /([A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+(\.[A-Za-z]{2,}))/gi;


document.querySelector('input[type="button"]').addEventListener('click',clicked);
function clicked(){
    let a = document.querySelector('textarea[name="your_message"]').value;
    let val = a.replace(reg,"<span style='color:red'>$1</span>");
    let outputFieldset = document.createElement('fieldset');
    outputFieldset.innerHTML = "<legend>Сообщение пользователей</legend>"+val
    document.querySelector('form').after(outputFieldset);
}
