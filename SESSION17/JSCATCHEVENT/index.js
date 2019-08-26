function startClick(){
    console.log("Start clicked");
}
var btn=document.getElementById('btn');
btn.textContent="Stop";
btn.addEventListener('click',startClick);
