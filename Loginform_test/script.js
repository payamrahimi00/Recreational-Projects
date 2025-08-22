let Username = document.querySelector("#username");
let Password = document.querySelector("#password");
let Module = document.querySelector("#beautiful-rectangle");
let Login_btn = document.querySelector("#Login_btn");

function Login() {
  if (Username.value.length >= 12 && Password.value.length >= 8) {
      Module.innerHTML = "Hello world!";
  } else {
      Module.innerHTML = "Invalid username or password!";
  }
}

Login_btn.addEventListener("click", Login);
