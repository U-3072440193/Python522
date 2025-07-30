document.writeln("<a href='#' class='show'>Показать</a>");
document.writeln("<a href='#' class='hide'>Спрятать</a>");
document.writeln("<img id='y' style='display:none; margin-bottom:10px;'>");
document.querySelector('img').style.display = 'block';
document.querySelector('img').style.marginBottom = '10px';

let show = document.querySelector('.show');
let image = document.getElementById('y')
show.onclick = function(){
    image.src = 'Capture.JPG';
    image.style.display = 'block';

};
let hide = document.querySelector('.hide');
hide.onclick = function(){
    image.src = '#';
    image.style.display = 'none';
}