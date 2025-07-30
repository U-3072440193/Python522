"use strict";
let  a = ["Январь","Февраль","Март","Апрель","Май","Июнь","Июль","Август","Сентябрь","Октябрь","Ноябрь","Декабрь"]

let createColor = () => {
    let r = Math.floor(Math.random() * 256);
    let g = Math.floor(Math.random() * 256);
    let b = Math.floor(Math.random() * 256);
    return `rgb(${r}, ${g}, ${b})`;
}
for (let i = 0; i < a.length; i++) {
    document.writeln(`<div class='block-${i}'>${a[i]}</div>`);
    let color = document.querySelector(`.block-${i}`);
    color.style.width = "400px";
    color.style.height = "100px";
    color.style.background = createColor();
    color.style.textAlign = "center";
}
