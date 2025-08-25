document.writeln("<img src='2.jpg' id='1'>");
document.writeln("<img src='3.jpg' id='2'>");
document.writeln("<img src='4.jpg' id='3'><br>");
document.writeln("<span>Поменять </span>");
document.writeln("<input type='number' min='1' max='3' class='one'> ");
document.writeln("<span>на </span>");
document.writeln("<input type='number' min='1' max='3' class='two'></br>");
document.writeln("<input type='button' class='btn' value='Поменять' style='margin:10px 10px;'>");




let btn = document.querySelector('.btn')
btn.addEventListener('click',replasing)

function replasing(){
    let valOne = document.querySelector('.one').value
    let valTwo = document.querySelector('.two').value
    if(valOne < 1 || valOne > 3 || valTwo < 1 || valTwo > 3){
    alert("Введите числа от 1 до 3");
    }
    let img1 = document.getElementById(valOne);
    let img2 = document.getElementById(valTwo);

    let temp = img1.src;
    img1.src = img2.src;
    img2.src = temp;
};