let Lamps = document.getElementById('Lampoff')
let Turn = false
let Btn = document.getElementById('btn')
function OfforOn(){
    if (Turn) {
        Lamps.setAttribute("src","./lamp2.jpg");
        Turn = false
        Btn.textContent = "OFF"

    } else  {
        Lamps.setAttribute("src","./lamp1.jpg");
        Lamps.classList.add('on')
        Turn = true
        Btn.textContent = "ON"

    }
}