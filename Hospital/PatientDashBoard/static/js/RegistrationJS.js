function Password(){
    let Passw=document.getElementById("PasswordID").value;
    console.log(Passw);
    if(Passw.length>7){
        document.getElementById("Password-error").innerHTML="Accept"
    }
    else{
        document.getElementById("Password-error").innerHTML="greater 7"
        return false
    }
}