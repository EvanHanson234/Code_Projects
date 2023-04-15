let number = 0;
let result = "";

function assignHead() {
  // Remove the 'let' keyword to update the value of the global variable instead of creating a new local variable
  number = 0;
}

function assignTail() {
  // Remove the 'let' keyword to update the value of the global variable instead of creating a new local variable
  number = 1;
}

function coinFlip() {
  // create a variable called coinFlip and assign it a random number between 0 and 1
  let coinFlip = Math.round(Math.random());

  // use a conditional to check the value of coinFlip
  // if the value is 0, print "Heads"
  if (coinFlip === 0) {
    console.log("Heads");
    if (coinFlip == number) {
      console.log("You win!");
      // Remove the 'let' keyword to update the value of the global variable instead of creating a new local variable
      result = "You guessed Heads...\n The coin flips and comes up Heads!\n Great Guess!";
    } else {
      console.log("You lose!");
      result = "You guessed Heads...\n The coin flips and comes up Tails :(\n Tough Loss!";
    }
  }
  // if the value is 1, print "Tails"
  else {
    console.log("Tails");
    if (coinFlip == number) {
      console.log("You win!");
      // Remove the 'let' keyword to update the value of the global variable instead of creating a new local variable
      result = "You guessed Tails...\n The coin flips and comes up Tails!\n Great Guess!";
    } else {
      console.log("You lose!");
      result = "You guessed Tails...\n The coin flips and comes up Heads :(\n Tough Loss!";
    }
  }

  let myTestElement = document.getElementById("result");
  myTestElement.innerHTML = result;
}
