var h1Id = document.querySelector('h1')
var buttonId = document.querySelector('button')
var counter = 0;
buttonId.addEventListener('click',function(){
    counter++
    h1Id.textContent = "Кликов сделано : " + counter 
})