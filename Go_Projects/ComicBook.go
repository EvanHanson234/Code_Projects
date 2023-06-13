package main

import "fmt"

func main() {
  var publisher string
  var writer string
  var artist string
  var title string
  var year int
  var grade float32
  var pageNum int

  //Book 1
  publisher = "DizzyBooks Publishing Inc."
  writer = "Tracey Hatchet"
  artist = "Jewel Tampson"
  title = "Mr. GoToSleep"
  year = 1997
  pageNum = 14
  grade = 6.5
  
  fmt.Println(title, "written by ", writer, "drawn by ", artist, "published by ", publisher, year, pageNum, grade)

  //Book 2
  publisher = "DizzyBooks Publishing Inc."
  writer = "Ryan N. Shawn"
  artist = "Phoebe Paperclips"
  title = "Epic Vol. 1"
  year = 2013
  pageNum = 160
  grade = 9.0

  fmt.Println(title, "written by ", writer, "drawn by ", artist, "published by ", publisher, year, pageNum, grade)
}