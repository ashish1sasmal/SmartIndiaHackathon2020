function signup(){
    document.getElementById("login").style.display="none"
    document.getElementById("sign_up").style.display="block"
}
function login(){
    document.getElementById("sign_up").style.display="none"
    document.getElementById("login").style.display="block"
 }
function final_signup(){
    if(document.getElementById("password").value != document.getElementById("again password").value){
        document.getElementById("alert").style.display="block"
    }
}