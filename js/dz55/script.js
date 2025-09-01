
let button = document.querySelector('input[type="button"]');

button.addEventListener('click',clicked);
function clicked(){
    let selected = document.form1.otv
    for(let i=0; i<selected.length;i++){
        if(selected[i].checked){
            let inner = selected[i].nextSibling.nodeValue
            alert(inner)
        }
    }

}
