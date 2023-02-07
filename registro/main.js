const nombre = document.getElementById("name");
const email= document.getElementById("email");
const usuario = document.getElementById("usuario");
const pass = document.getElementById("password");


const form = document.getElementById("form")
const parrafo = document.getElementById("warnings")


form.addEventListener("submit", e=>{
    e.preventDefault()
    let warnings =""
    let entrar = false 
    let regexEmail = /^\w+([\.-]?\w+)*@\w+([\.-]?\w+)*(\.\w{2,3})+$/
    parrafo.innerHTML=""
    if(nombre.value.length <6){
        warnings += `El nombre no es valido <br>`
        entrar= true
    }
    if(!regexEmail.test(email.value)){
        warning += `El nombre no es valido <br>`
        entrar = true

    }
    if(pass.value.lenghth <8){
        warning += `La contraseña no es valida <br>`
        entrar = true

    }
    if(entrar){
        parrafo.innerHTML = warning
    }else{
        parrafo.innerHTML= "Enviado"
    }
})