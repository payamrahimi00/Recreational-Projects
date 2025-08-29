<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Body Color Timer</title>
    <style>
        /* --- Body and layout --- */
        body {
            display: flex;
            flex-direction: column; /* text and button stacked */
            justify-content: center;
            align-items: center;
            width: 100vw;
            height: 100vh;
            margin: 0;
            transition: background-color 0.5s ease; /* smooth color change */
        }

        /* --- Text styling --- */
        .center {
            font-size: 2.6rem;
            margin-bottom: 20px;
            color: white;
            text-align: center;
        }

        /* --- Background colors --- */
        .red { background-color: red; }
        .blue { background-color: blue; }
        .green { background-color: green; }

        /* --- Button styling --- */
        .btn {
            background-color: #fff;
            border-radius: 5px;
            font-size: 2rem;
            padding: 10px 20px;
            cursor: pointer;
            border: none;
        }
    </style>
</head>
<body class="red">
    <h1 class="center">Payam Rahimi</h1>
    <button class="btn" id="stopBtn">Stop</button>

    <script>
        let Body_elem = document.querySelector('body');
        let StopBtn = document.getElementById('stopBtn');
        let Timer;
        let count = 0;

        // Start interval when body is clicked
        Body_elem.addEventListener("click", () => {
            // Prevent creating multiple intervals
            if (Timer) return;

            Timer = setInterval(() => {
                if (count == 1) {
                    Body_elem.classList.add("red");
                    Body_elem.classList.remove("blue", "green");
                } else if (count == 6) {
                    Body_elem.classList.add("blue");
                    Body_elem.classList.remove("red", "green");
                } else if (count == 11) {
                    Body_elem.classList.add("green");
                    Body_elem.classList.remove("red", "blue");
                } else if (count == 17) {
                    count = 0; // reset counter
                }

                count++;
                console.log(count);
            }, 1000);
        });

        // Stop interval when stop button is clicked
        StopBtn.addEventListener("click", (event) => {
            event.stopPropagation(); // prevent body click from firing
            clearInterval(Timer);
            Timer = null; // reset so it can start again
            console.log("Stopped!");
        });
    </script>
</body>
</html>
