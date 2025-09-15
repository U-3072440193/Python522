

let ii = document.querySelector("#rub");
let iw = document.querySelector("#usd");
let ie = document.querySelector("#euro");

ii.addEventListener("input",()=>{
  let req = new XMLHttpRequest();
  req.open("GET","current.json");
  req.setRequestHeader("content-type","application/json; charset=utf-8");
  req.send();
  req.addEventListener("readystatechange",()=>{
    if(req.status == 200){
      let data = JSON.parse(req.response);
      iw.value = (ii.value/data.current.usd).toFixed(2)
      ie.value = (ii.value/data.next.euro).toFixed(2)
    }else{iw.value ="Ошибка"};
  })

})