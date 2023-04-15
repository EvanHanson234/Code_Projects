let result = "";
let maxNumber = 0;
let guesses = [];   //array to store the guesses
let win = "You won!";
let gameEnd = false;


// Prompt the user to enter a maximum number
maxNumber = prompt("Enter a maximum number");
validitate();

// Validate the user's input, and round it to the nearest integer
function validitate() {
  while (isNaN(maxNumber) || maxNumber === "" || maxNumber <= 0) {
    maxNumber = prompt("Enter a valid number");
  }
}
maxNumber = Math.round(parseFloat(maxNumber));    //rounds the number to the nearest integer
document.getElementById("maxNumber").innerHTML = maxNumber;



// Generate a number between 1 and maxNumber
let randomNumber = Math.floor(Math.random() * maxNumber) + 1;

function checkGuess() {
  // Check if the game is over
  if (gameEnd) {
    return;
  }

  // Empty the result and error messages
  document.getElementById("result").innerHTML = "";
  document.getElementById("error").innerHTML = "";

  // Get the value of the input field
  let guess = document.getElementById("guess").value;

  // Validate the user's input, and check if it is in range
  while (isNaN(guess) || guess === "" || guess < 1 || guess > maxNumber) {
    if (isNaN(guess) || guess === "") {
      //Display an error message
      result = "That's not a number!";
    } else if (guess < 1 || guess > maxNumber) {
      //Display an error message
    result = "That number is not in range, try again. Please enter a valid number between 1 and " + maxNumber;
    }

    document.getElementById("error").innerHTML = result;   // Display the result
    return;  // Exit the function
  }


  // Check if the guess has been done before
  if (guesses.includes(guess)) {
    result = "You already guessed that number. Try again.";
    document.getElementById("error").innerHTML = result;   // Display the result
    return;  // Exit the function
  }

  
  // Check if the guess is correct
  if (guess == randomNumber) {
    let guessNumber = guesses.length + 1;
    // Add the guess to the array
    guesses.push(guess);
    result = "You guessed correctly! It took you " + guessNumber + " guesses." + "<br>" + "Your guesses were: " + guesses;
    document.getElementById("win").innerHTML = win;
    gameEnd = true;

  } else if (guess > randomNumber) {
    result = "Your guess is too high. Try again.";
    // Add the guess to the array
    guesses.push(guess);

  } else if (guess < randomNumber) {
    result = "Your guess is too low. Try again.";
    // Add the guess to the array
    guesses.push(guess);
  }

  // Display the result
  document.getElementById("result").innerHTML = result;
}