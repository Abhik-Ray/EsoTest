let text = document.querySelector('h1');
let textStr = null;
let splitText = null;
let char = 0;
let flag = 0;
let pos = [];
const vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'];
const glitch = ['#', '@', '?', '&', '=', ';', 't'];


window.onload = function () { 
    text = document.querySelector('h1');
    textStr = text.textContent;
    splitText = textStr.split("");
    
    text.textContent = "";

    for(let i = 0; i < splitText.length; i++){
        text.innerHTML += "<span>" + splitText[i] + "</span>";
    }

    let timer = setInterval(function () {
        const span = text.querySelectorAll('span')[char];
        span.classList.add('fade');
        if(vowels.includes(span.textContent)){
            pos.push(char);
        }
        char++;
        if(char === splitText.length){
            complete();
            return;
        }
    }, 300);
    let timer2 = setInterval(function () {
        for(i=0;i<pos.length;i++){
            let str = document.querySelectorAll('span')[pos[i]];
            str.textContent = glitch[Math.floor(Math.random() * 6)];
        }
    }, 100);
 }

function complete(){
    clearInterval(timer);
    timer = null;
}