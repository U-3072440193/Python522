let request = new XMLHttpRequest();
request.open("GET","data.txt"); 
request.send();
request.onreadystatechange = function(){
  if((request.readyState ==4)&&(request.status == 200)){document.writeln(request.response);}
}