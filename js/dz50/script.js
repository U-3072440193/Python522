document.writeln("<div id='one'></div>");

let a = document.querySelector('#one')
a.innerHTML = `о временем программы становятся всё сложнее и сложнее. Возникает необходимость добавлять комментарии, которые бы описывали, что делает код и почему.\

Комментарии могут находиться в любом месте скрипта. Онине влияют на его выполнение, поскольку движок просто игнорирует их.\

Однострочные комментарии начинаются с двойной косой черты.`;
a.style.backgroundColor = 'yellow';
a.style.color = 'black';
a.style.width = '256px';
a.style.height = '256px';
a.style.overflow = 'scroll';
a.style.outline = '1px dashed red';
a.className = "resetFont";
let cl = document.querySelector(".resetFont")
cl.style.fontSize = '20px';
a.style.fontWeight = '400';
a.style.textDecoration = 'underline';
