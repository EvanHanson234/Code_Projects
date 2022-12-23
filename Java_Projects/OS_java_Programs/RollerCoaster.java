/*	
	Roller Coaster Problem
	Written by Evan Hanson
	December 15th, 2022		
*/

/*	
	Problem:
	The Roller Coaster problem: Suppose there are n passenger threads (e.g. 10) 
	and one car thread. The passengers repeatedly wait to take rides in the car, 
	which can hold C passengers (e.g. 4), C < n. However, the car can only go 
	around the tracks when it is full. The car will wait in the station until it 
	fills up before going around the track. The car takes the same T seconds 
	(e.g. 6 seconds) to go around the track each time it fills up. After getting 
	a ride, each passenger wanders (nap) around the amusement park for a random 
	amount of time (between 0 and W seconds; e.g. 5) before returning to the roller 
	coaster for another ride.

   What Works and Not:
   - Creates passengers and a car.
   - Is able to itterate through in random intervals to see how long the passengers last.
   - I have the functionality of the problem more or less working... The big issue is
   that even through I have the car fill up, the passengers that "finish" the ride are
   not always the ones that were in line first. Sometimes the passengers that come 
   to the line later will be the ones that "finish" the ride.

   Overall it was fun trying to work through this problem and relearn Java again.
*/

import Utilities.*;
class RollerCoaster extends MyObject {
  public static void main(String[] args) {
	final int PASSENGERS = 10;
	final int CAR = 1;
    int runTime = 5;      // seconds
    Thread[] passengers = new Thread[PASSENGERS];
    Thread[] cars = new Thread[CAR];
    // create the RollerCoasterServer object
    RollerCoasterServer rcServer = new RollerCoasterServer();
    // create the passengers
    for (int i = 0; i < PASSENGERS; i++) {
       passengers[i] = new Thread(new Passenger("passengers", i, rcServer));
       passengers[i].start();
    }
    System.out.println("All passenger threads started");
    // create the car
    for (int i = 0; i < CAR; i++) {
       cars[i] = new Thread(new Car("car", i, rcServer));
       cars[i].start();
    }
    System.out.println("Car thread started");
    // let it run for a while
    nap(runTime*1000);
    System.out.println("age()=" + age() + ", time to stop the EVERYTHING and exit");
    for (int i = 0; i < PASSENGERS; i++)
     passengers[i].interrupt();
    for (int i = 0; i < CAR; i++)
     cars[i].interrupt();
    System.exit(0);
  }
}
class Passenger extends MyObject implements Runnable {
   private int id = 0;
   private RollerCoasterServer rcServer = null;
   final int MAXREADTIME = 20;
   final int MAXINTERREADTIME = 45;
   public Passenger(String name, int id, RollerCoasterServer rcServer) {
      super(name + " " + id);
      this.id = id;
      this.rcServer = rcServer;
      System.out.println(getName() + " is alive");
   }
   public void run() {
      while (true) {
         nap((int) random(MAXINTERREADTIME));
         rcServer.StartPassenger(id);
         nap((int) random(MAXREADTIME));
         rcServer.EndPassenger(id);
      }
   }
}
class Car extends MyObject implements Runnable {
   private int id = 0;
   private RollerCoasterServer rcServer = null;
   final int MAXWRITETIME = 10;
   final int MAXINTERWRITETIME = 35;
   public Car(String name, int id, RollerCoasterServer rcServer) {
      super(name + " " + id);
      this.id = id;
      this.rcServer = rcServer;
      System.out.println(getName() + " is alive");
   }
   public void run() {
      while (true) {
         nap((int) random(MAXINTERWRITETIME));
         rcServer.StartCar(id);
         nap((int) random(MAXWRITETIME));
         rcServer.EndCar(id);
      }
   }
}  
class RollerCoasterServer extends MyObject {
   final int CAPACITY = 4;          //car capacity
   private int passengerCount = 0;  //number of passengers in the car while waiting
   private int waitCount = 0;       //number of people waiting -- not in use anynmore.
   private int riderCount = 0;      //number of riders in the car while riding
   private boolean riding = false;  //is the car riding?
   public RollerCoasterServer() {
      System.out.println("RollerCoasterServer Started");
   }
   public synchronized void StartPassenger(int i) {
      //waitCount ++;
      System.out.println("age()=" + age() + " Passenger " + i + " is waiting to ride" );
      if (passengerCount < CAPACITY && riderCount == 0) {    //is the car still empty?
         passengerCount ++;
         //waitCount --;
         System.out.println("age()=" + age() + " Passenger " + i + " entered the Car" );
         if (passengerCount == CAPACITY) {
            System.out.println("age()=" + age() + " We are at CAPACITY" );    //let us know when we are at capacity
         }
      }
      notifyAll();
   }
   public synchronized void StartCar(int i) {
      while (passengerCount == CAPACITY){    //if the car is full and ready to ride
         riding = true;
         System.out.println("age()=" + age() + " Car " + i + " is riding");
         passengerCount = passengerCount - 4;   //people transition from passengers to riders
         riderCount = riderCount + 4;
         //try {wait();} catch (InterruptedException e) {}
         notifyAll();
      }
      while (passengerCount < CAPACITY) {    //if the car is not full
         System.out.println("age()=" + age() + " Car " + i + " is waiting to fill up");
         try {wait();} catch (InterruptedException e) {}
      }
   }
   public synchronized void EndPassenger(int i) {
      if (riding == true && riderCount > 0){   
         //System.out.println(" passengerCount=" + passengerCount + " riderCount=" + riderCount); //debug to see number of passengers and riders
         riderCount --;
         System.out.println("age()=" + age() + " Passenger " + i + " is done riding");
      }
      notifyAll();
   }
   public synchronized void EndCar(int i) {
      if (riding == true){
         riding = false;
         System.out.println("age()=" + age() + " Car " + i + " is done riding");
      }
      notifyAll();
   }   
}  