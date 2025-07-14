let price = +prompt('ВВедите стоимость покупки')
let s
let summ
if (price > 500 && price < 1000){
    let s = 3
    let summ = price + (price*(s/100))
    alert("Стоимость покупки без скидки "+price+'рублей. Скидка '+s+'%. Итоговая стоимость '+summ+' рублей.')
}
else if(price > 100 ){
    let s = 5
    let summ = price + (price*(s/100))
    alert("Стоимость покупки без скидки "+price+'рублей. Скидка '+s+'%. Итоговая стоимость '+summ+' рублей.')
}
else {alert('Для таких цен никаких скидок не предусмотрено')}