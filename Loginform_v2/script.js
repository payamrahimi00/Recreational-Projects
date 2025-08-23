let Username = document.querySelector("#username");
let Password = document.querySelector("#password");
let Module = document.querySelector("#beautiful-rectangle");
let Login_btn = document.querySelector("#Login_btn");
let labels = document.getElementsByClassName('my_mark')



function Login() {
  if (Username.value.length < 12) {
      labels[0].style.display = 'block'
  
  } else{
          labels[0].style.display = 'none'

  }

   if(Password.value.length < 8) {
      labels[1].style.display = 'block'
  } else {
      labels[1].style.display = 'none'

  }

    }

Login_btn.addEventListener("click", Login);