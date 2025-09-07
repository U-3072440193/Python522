
function Person(name,age,job){
    this.name = name;
    this.age = age;
    this.job = job;

    this.who= function(){
        document.writeln(`<span>Я <strong>${this.name}</strong>, мне <strong>${this.age}</strong> лет. 
            Я работаю <strong>${this.job}ом</strong>.</span><br>`);
    };
};

let Dmitr = new Person("Дмитрий", "26", "дизайнер");
Dmitr.who();
let Stan = new Person("Станислав", "29", "программист");
Stan.who();
let Sergo = new Person("Сергей", "35", "менеджер");
Sergo.who();