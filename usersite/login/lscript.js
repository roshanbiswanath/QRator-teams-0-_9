function validation(){
    let x = document.forms["myForm"]["uname"].value;
    if (x == "") {
      alert("Name must be filled out");
      return false;
    }
    let p = document.forms["myForm"]["pas"].value;
    if(p == ""){
        alert("enter password");
      return false;
    }
}
