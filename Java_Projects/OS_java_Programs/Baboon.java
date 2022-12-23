/*	
	Baboon Problem
	Written by Evan Hanson
	December 15th, 2022		
*/

/*	
	Problem:
   A canyon cuts through the territory of a colony of baboons. 
   The baboons use a rope stretching across the canyon to cross 
   from one side to the other. The rope is strong enough to permit 
   any number of baboons to cross in the same direction at the same 
   time. However, the rope is too thin for the baboons to cross the 
   canyon in both directions at the same time. Consequently, a baboon 
   that wants to cross from west to east must wait until all westward-moving 
   baboons have finished crossing and the rope is free.

    What Works and Not:
   - Creates East and West Baboon threads.
   - Is able to itterate through in random intervals to see how long the baboons last.
   - I think this solution can have starvation.
   - Similar to the RollarCoaster problem, I have the functionality of the problem more 
   or less working... The issue is that I don't think that exclusively wait long enough for 
   one side of baboons to finish be stating that their side is finished.

   Overall it was fun trying to work through this problem and relearn Java again.
*/

import Utilities.*;
class Baboons extends MyObject {
   public static void main(String[] args) {
      final int EAST = 5;
      final int WEST = 10;
      int runTime = 5;      // seconds
      Thread[] eastBabs = new Thread[EAST];
      Thread[] westBabs = new Thread[WEST];
      // create the BaboonServer object
      BaboonServer babServer = new BaboonServer();
      // create the EastBab
      for (int i = 0; i < EAST; i++) {
         eastBabs[i] = new Thread(new Baboon("EastBab", i, babServer));
         eastBabs[i].start();
      }
      System.out.println("All EastBab threads started");
      // create the westBab
      for (int i = 0; i < WEST; i++) {
         westBabs[i] = new Thread(new Baboon("WestBab", i, babServer));
         westBabs[i].start();
      }
      System.out.println("All WestBab threads started");
      // let the program run for a while
      nap(runTime*1000);
      System.out.println("age()=" + age() + ", time to stop the East/West and exit");
      for (int i = 0; i < EAST; i++)
         eastBabs[i].interrupt();
      for (int i = 0; i < WEST; i++)
         westBabs[i].interrupt();
      System.exit(0);
  }
}
class Baboon extends MyObject implements Runnable {
   private int id = 0;
   private BaboonServer babServer = null;
   final int MAXREADTIME = 20;
   final int MAXINTERREADTIME = 45;
   public Baboon(String name, int id, BaboonServer babServer) {
      super(name + " " + id);
      this.id = id;
      this.babServer = babServer;
      System.out.println(getName() + " is alive");
   }
   public void run() {
      while (true) {
         nap((int) random(MAXINTERREADTIME));
         babServer.StartEast(id);
         nap((int) random(MAXREADTIME));
         babServer.EndEast(id);

         nap((int) random(MAXINTERREADTIME));
         babServer.StartWest(id);
         nap((int) random(MAXREADTIME));
         babServer.EndWest(id);
      }
   }
}    
class BaboonServer extends MyObject {
   public boolean eastCrossing = false;
   public boolean westCrossing = false;
   public BaboonServer() {
      System.out.println("BaboonServer Started");
   }
   public synchronized void StartEast(int i) {
      System.out.println("age()=" + age() + " East " + i + " wants to cross" );     //an east baboon waits to cross
      while (westCrossing) {     //if a west baboon is currently crossing, the east ones will have to wait
         try {wait();} catch (InterruptedException e) {}
      }
      eastCrossing = true;   
      System.out.println("age()=" + age() + " East " + i + " is about to cross" );  //east baboon crossing
   }
   public synchronized void StartWest(int i) {
      System.out.println("age()=" + age() + " West " + i + " wants to cross");      //a west baboon waits to cross
      while (eastCrossing) {     //if an east baboon is curently crossing, the west ones will have to wait
         try {wait();} catch (InterruptedException e) {}
      }
      westCrossing = true;
      System.out.println("age()=" + age() + " West " + i + " is about to cross");   //west baboon crossing
   }
   public synchronized void EndEast(int i) {
      eastCrossing = false;      //east baboon is done crossing. They reset.
      notifyAll();
      System.out.println("age()=" + age() + " East " + i + " is done crossing");
   }
   public synchronized void EndWest(int i) {
      westCrossing = false;      //west baboon is done crossing. They reset.
      notifyAll();
      System.out.println("age()=" + age() + " West " + i + " is done crossing");
   }
}