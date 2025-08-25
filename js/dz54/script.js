let btn = document.querySelectorAll('.remove-button');
for(let b = 0; b < btn.length; b++){
    btn[b].addEventListener('click',remove);
    function remove(){this.parentNode.remove()};
    
};



