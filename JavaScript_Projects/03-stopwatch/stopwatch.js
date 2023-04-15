let seconds = 00;
let minutes = 00;
let hours = 00;
let running = false;      // running is used to check if the timer is running or not
let timerId = null;       // timerId is used to stop the timer interval


// When clicked, the button will start the stopwatch
function start() {
  if (!running) {          // if running is false, then start the timer
    running = true;        // now running
    timerId = setInterval(runClock, 1000); // runs the runClock function every second
  }
}

// This function runs every second - becasue of the setInterval() function
function runClock() {
  seconds += 1;
  if (seconds == 60) {     // if seconds is 60, add 1 to minutes and reset seconds to 0
    minutes += 1;
    seconds = 0;
  }
  if (minutes == 60) {     // if minutes is 60, add 1 to hours and reset minutes to 0
    hours += 1;
    minutes = 0;
  }
  if (hours == 24) {        // if hours is 24, reset to 0
    hours = 0;
  }

  let displaySeconds = seconds < 10 ? "0" + seconds : seconds; // if seconds is less than 10, add a 0 in front of it
  let displayMinutes = minutes < 10 ? "0" + minutes : minutes; // if minutes is less than 10, add a 0 in front of it
  let displayHours = hours < 10 ? "0" + hours : hours;         // if hours is less than 10, add a 0 in front of it

  document.getElementById("time").innerHTML = displayHours + ":" + displayMinutes + ":" + displaySeconds;
}

// When clicked, the button will stop the stopwatch
function stop() {
  if (running) {            // if running is true, then stop the timer
    running = false;        // no longer running
    clearInterval(timerId); // stops the timer interval
  }
}

// When clicked, the button will reset the stopwatch
function reset() {
  stop();                   // stop the timer
  seconds = 0;
  minutes = 0;
  hours = 0; 
  document.getElementById("time").innerHTML = "00:00:00"; // reset the timer to 00:00:00
}