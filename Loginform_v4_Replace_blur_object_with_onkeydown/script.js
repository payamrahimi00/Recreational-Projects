let Username = document.querySelector("#username");
let Password = document.querySelector("#password");
let Module = document.querySelector("#beautiful-rectangle");
let Login_btn = document.querySelector("#Login_btn");
let alerts = document.getElementsByClassName("Event");

function correctUserkeydown() {
    if(Username.value.length > 10) {
        alerts[0].innerHTML = "User is valid"
        alerts[0].style.color = "green"
    } else {
        alerts[0].innerHTML = "Charachter must grater than 12";
        alerts[0].style.color = "red"
    }
}
function correctPasskeydown() {
        if(Password.value.length >= 7) {
        alerts[1].innerHTML = "Password is valid"
        alerts[1].style.color = "green"
    } else {
        alerts[1].innerHTML = "Your password is wrong";
        alerts[1].style.color = "red"
    }
}

// function Login() {
//     }

// Login_btn.addEventListener("click", Login);