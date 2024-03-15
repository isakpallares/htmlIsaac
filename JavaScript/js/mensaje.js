document.getElementById("enlace").addEventListener("click",()=> {
    let ele = document.querySelector("#mensaje");
    if(ele.className=="mensajeoculto"){
        ele.className="mensajevisible";
    }else{
        ele.className="mensajeoculto"
    }
})