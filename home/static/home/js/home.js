function changeState(){
    let stat = document.querySelector("#state")
    let stateValue = document.querySelector('#state').textContent
   
    if (stateValue=='On'){
        stat.textContent = "Off";
        stat.style.background='green' 
    }
    else{
        stat.textContent = "On";
        stat.style.background = 'black';
        stat.style.color='white';
    }

  
}

function submitForm(element){
    let buttonValue = element.textContent
    
    let id = element.getAttribute('id')
    console.log(id)

    let input = document.createElement("input")
    input.setAttribute('name',String(id));
    input.setAttribute('type','text');
    input.style.display="none"
    input.setAttribute('value',String(buttonValue))
    let form = document.querySelector("#myform")
    form.appendChild(input)
    form.submit()
}

  
document.addEventListener('DOMContentLoaded',function(event){

   
let div = document.querySelector(".buttons");
let stat =document.getElementsByClassName("state")

console.log(stat.length)
let stateValue = stat.textContent
console.log("checking",stateValue)


for(let i=0;i<stat.length;i++){

    let element  =stat[i]
    let elementValue = element.textContent;

    console.log(typeof(elementValue))

    if (elementValue.trim()=="On"){
        element.style.background="green";
        element.style.color="white";
    }else{
        element.style.background="black";
        element.style.color="white";
    
    }
 

    
   
 

}


  


})
