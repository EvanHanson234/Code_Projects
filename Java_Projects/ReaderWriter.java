/*	
	Baboon Crossing Problem
	Written by Evan Hanson
	December 1st, 2022		
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
*/

import Utilities.*;
class ReadersWriters extends MyObject {
  public static void main(String[] args) {
    final int NUMREADERS = 5;
    final int NUMWRITERS = 10;
    int runTime = 5;      // seconds
    Thread[] readers = new Thread[NUMREADERS];
    Thread[] writers = new Thread[NUMWRITERS];
    // create the ReaderWriterServer object
    ReaderWriterServer rwServer = new ReaderWriterServer();
    // create the readers
    for (int i = 0; i < NUMREADERS; i++) {
       readers[i] = new Thread(new Reader("Reader", i, rwServer));
       readers[i].start();
    }
    System.out.println("All Reader threads started");
    // create the writers
    for (int i = 0; i < NUMWRITERS; i++) {
       writers[i] = new Thread(new Writer("Writer", i, rwServer));
       writers[i].start();
    }
    System.out.println("All Writer threads started");
    // let the readers and writers run for a while
    nap(runTime*1000);
    System.out.println("age()=" + age() + ", time to stop the readers/writers and exit");
    for (int i = 0; i < NUMREADERS; i++)
     readers[i].interrupt();
    for (int i = 0; i < NUMWRITERS; i++)
     writers[i].interrupt();
    System.exit(0);
  }
}
class Reader extends MyObject implements Runnable {
   private int id = 0;
   private ReaderWriterServer rwServer = null;
   final int MAXREADTIME = 20;
   final int MAXINTERREADTIME = 45;
   public Reader(String name, int id, ReaderWriterServer rwServer) {
      super(name + " " + id);
      this.id = id;
      this.rwServer = rwServer;
      System.out.println(getName() + " is alive");
   }
   public void run() {
      while (true) {
         nap((int) random(MAXINTERREADTIME));
         rwServer.StartReader(id);
         nap((int) random(MAXREADTIME));
         rwServer.EndReader(id);
      }
   }
}    
class Writer extends MyObject implements Runnable {
   private int id = 0;
   private ReaderWriterServer rwServer = null;
   final int MAXWRITETIME = 10;
   final int MAXINTERWRITETIME = 35;
   public Writer(String name, int id, ReaderWriterServer rwServer) {
      super(name + " " + id);
      this.id = id;
      this.rwServer = rwServer;
      System.out.println(getName() + " is alive");
   }
   public void run() {
      while (true) {
         nap((int) random(MAXINTERWRITETIME));
         rwServer.StartWriter(id);
         nap((int) random(MAXWRITETIME));
         rwServer.EndWriter(id);
      }
   }
}    
class ReaderWriterServer extends MyObject {
   private int readCount = 0;
   private boolean writing = false;
   public ReaderWriterServer() {
      System.out.println("ReaderWriterServer Started");
   }
   public synchronized void StartReader(int i) {
    readCount ++;
System.out.println("age()=" + age() + " Reader " + i + " wants to read" );
while (writing) {
  try {wait();} catch (InterruptedException e) {}
}
      
System.out.println("age()=" + age() + " Reader " + i + " is about to read" );
   }
   public synchronized void StartWriter(int i) {
System.out.println("age()=" + age() + " Writer " + i + " wants to write");
    while ((readCount > 0) || writing) {
  try {wait();} catch (InterruptedException e) {}
}
writing = true;
System.out.println("age()=" + age() + " Writer " + i + " is about to write");
   }
   public synchronized void EndReader(int i) {
    readCount --;
    if (readCount == 0) {
        notifyAll();
    }
      
System.out.println("age()=" + age() + " Reader " + i + " is done reading");
   }
   public synchronized void EndWriter(int i) {
    writing = false;
    notifyAll();
      
System.out.println("age()=" + age() + " Writer " + i + " is done writing");
   }   
}