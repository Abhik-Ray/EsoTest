$(document).ready(function(){
    $("#theme-button").click(function(){
        let theme;
        $("html").attr("data-theme") === "light" ? theme="dark" : theme="light";
        $("html").attr("data-theme", theme);
    });
});
const text = document.querySelector('h1');
const textStr = text.textContent;
const splitText = textStr.split("");

text.textContent = "";

for(let i = 0; i < splitText.length; i++){
    text.innerHTML += "<span>" + splitText[i] + "</span>";
}

let char = 0;
let timer = setInterval(onTick, 300);
let timer2 = setInterval(scramble, 100);
let flag = 0;
let pos = [];
const vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'];
const glitch = ['#', '@', '?', '&', '=', ';', 't'];
function onTick(){
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
}

function scramble(){
    for(i=0;i<pos.length;i++){
        let str = document.querySelectorAll('span')[pos[i]];
        str.textContent = glitch[Math.floor(Math.random() * 6)];
    }
}

function complete(){
    clearInterval(timer);
    timer = null;
}