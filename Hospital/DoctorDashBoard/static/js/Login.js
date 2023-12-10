function EmailError(){
    let Password=document.getElementById("PasswordID").value;
    console.log(Password);
    if(Password.lenght>7){
        console.log(Password);
        return false
    } 
    else{
        return true
    }

}