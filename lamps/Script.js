function Btn() {
    const lamps = document.querySelectorAll('.lamps');
    lamps[0].style.display = 'block'; // Show ON lamp
    lamps[1].style.display = 'none';  // Hide OFF lamp
}

function Btn2() {
    const lamps = document.querySelectorAll('.lamps');
    lamps[0].style.display = 'none';  // Hide ON lamp
    lamps[1].style.display = 'block'; // Show OFF lamp
}

function Default() {
    const lamps = document.querySelectorAll('.lamps');
    // Reset both images to default
    lamps[0].src = 'lamp1.jpg'; // ON lamp
    lamps[1].src = 'lamp2.jpg'; // OFF lamp
    // Reset display (if needed)
    lamps[0].style.display = 'block';
    lamps[1].style.display = 'block';
}