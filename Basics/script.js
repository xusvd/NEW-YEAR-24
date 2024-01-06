// alert("Happy New year!🥳🥳")
console.log("Wecome!");
let hCount=0
function sendHeart(){
    
    let uName= document.getElementById("userName").value;
    console.log(uName);
    hCount=hCount+1
    document.getElementById("two").append(`${hCount}. ${uName} is Awesome 🥰 `)
}
