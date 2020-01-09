function signup(){
    document.getElementById("login").style.display="none"
    document.getElementById("sign_up").style.display="block"
}
function login(){
    document.getElementById("sign_up").style.display="none"
    document.getElementById("login").style.display="block"
}
function ask_pass(){
    var username="Default User";
    document.getElementById("sign_up").style.display="none"
    document.getElementById("signup_final").style.display="block"
    //assign variable "username" a value which will be used to display...
    document.getElementById("user_span").innerHTML=username.bold()
}
function final_signup(){
    if(document.getElementById("password").value != document.getElementById("again password").value){
        document.getElementById("alert").style.display="block"
    }
}