let clockType12 = false;
let clockTypeText = "12-hour clock";

function clock() {
    let today = new Date();
    let day = today.getDate();
    let month = today.getMonth() + 1; // add 1 to get the correct month
    let year = today.getFullYear();
    let seconds = today.getSeconds();
    let minutes = today.getMinutes();
    let hours = today.getHours();
  
    // add leading zeros to single-digit numbers
    if (hours < 10) {
      hours = "0" + hours;
    }
    if (minutes < 10) {
      minutes = "0" + minutes;
    }
    if (seconds < 10) {
      seconds = "0" + seconds;
    }

    // make it a 12-hour clock
    if (clockType12) {
        if (hours > 12) {
            hours = hours - 12;
            
        }
        clockTypeText = "24-hour clock";
        
    } else {
        clockTypeText = "12-hour clock";
    }
  
    let date = month + '-' + day + '-' + year;
    let time = hours + ":" + minutes + ":" + seconds;
  
    document.getElementById("time").innerHTML = time;
    document.getElementById("date").innerHTML = date;

    document.getElementById("clockTypeText").innerHTML = clockTypeText;
  }
  
  // clockType button pressed
function clockType() {
    clockType12 = !clockType12;
}

  setInterval(clock, 1000);