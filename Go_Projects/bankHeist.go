package main

import (
  "fmt"
  "math/rand"
  "time"
)

func main() {
  rand.Seed(time.Now().UnixNano())

  var isHeistOn = true
  var eludedGuards = rand.Intn(100)

  //Step 1
  if eludedGuards >= 50 {
    fmt.Println("Looks like you've managed to make it past the guards. Good job, but remember, this is the first step.")
  } else {
    isHeistOn = false
    fmt.Println("Plan a better disguise next time?")
  }

  var openedVault = rand.Intn(100)

  //Step 2
  if isHeistOn && openedVault >=70 {
    fmt.Println("Grab and Go!")
  } else if isHeistOn {
    isHeistOn = false
    fmt.Println("Vault can't be opened.")
  }

  var leftSafely = rand.Intn(5)

  //Step 3
  if isHeistOn {
    switch leftSafely {
      case 0:
      isHeistOn = false
      fmt.Println("Did not leave safely.")
      case 1:
      isHeistOn = false
      fmt.Println("Vault doors dont opend from the inside... you're stuck.")
      case 2:
      isHeistOn = false
      fmt.Println("Cops got ya.")
      case 3:
      isHeistOn = false
      fmt.Println("The security camera caught you.")
      default:
      fmt.Println("Start the getaway car!")
    }
  }

  var amtStolen = 10000 + rand.Intn(1000000)

  //Step 4
  if isHeistOn {
    fmt.Println("Money you stole: ", amtStolen)
  }

  //fmt.Println("Is the Heist on? --> ", isHeistOn)

}
