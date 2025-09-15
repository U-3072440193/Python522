let form = document.form1;
let message = {
    loading: "Загрузка",
    success: "Спасибо! Скоро мы с вами свяжемся",
    failure: "Что-то пошло не так"
};

form.addEventListener("submit", event =>{
    event.preventDefault();

    let msg = document.createElement("div");
    msg.style.position = "fixed";
    msg.style.top = "0";
    msg.style.left = "0";
    msg.style.width = "100%";
    msg.style.height = "100%";
    msg.style.display = "flex";
    msg.style.background = "rgba(241, 141, 141, 0.5)";
    msg.style.alignItems = "center";
    msg.style.justifyContent = "center";
    msg.style.zIndex = "9999"; 

    
    let modal = document.createElement("div");
    modal.style.backgroundColor = "rgba(255, 255, 255, 1)"
    modal.style.padding = "30px 50px";
    modal.style.maxWidth = "90%";
    modal.style.textAlign = "center";

    
    let text = document.createElement("div");
    text.textContent = message.loading;

    modal.appendChild(text);
    msg.appendChild(modal);

    
    document.body.appendChild(msg);
    let request = new XMLHttpRequest();
    request.open("POST","server.php");
    let formData = new FormData(form);
    request.send(formData);
    request.addEventListener("load", function(){
        if(request.status == 200){
            console.log(request.response)
            text.textContent = message.success;
        }else{
          text.textContent = message.failure
        }
        form.reset();
        setTimeout(()=>msg.remove(), 3000)
    })
})