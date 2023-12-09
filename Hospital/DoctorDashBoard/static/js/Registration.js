function FirstNameError(){
    let FirstNameError=document.getElementById("FirstNameID").value;
    console.log(FirstNameError);
    if (FirstNameError===" " | FirstNameError==""){
        document.getElementById("FirstName-error").innerHTML="Invalid First Name";
        return false
    }
    else{
        document.getElementById("FirstName-error").innerHTML="";
        return true
    }

}

function PasswordError(){
    let Passw=document.getElementById("PasswordID").value;
    console.log(Passw);
    if(Passw.length>7){
        document.getElementById("PasswordID-error").innerHTML="Accept"
    }
    else{
        document.getElementById("PasswordID-error").innerHTML="greater 7"
        return false
    }
}

function CpasswordError(){
    let Passw=document.getElementById("PasswordID").value;
    let CPassw=document.getElementById("CPasswordID").value;
    console.log(Passw,CPassw);
    if (Passw===CPassw){
        document.getElementById("CPassw-error").innerHTML="Password match";
        return true
    }
    else{
        document.getElementById("CPassw-error").innerHTML="Password didn't match";
        return false
    }
}