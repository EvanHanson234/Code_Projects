/*	
	Rollar Coaster Problem
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

class ReaderWriter {
   private int numReaders = 0;
   private int numWriters = 0;
   private int mutex = 1;
   private int wrt = 1;
   
   private synchronized void prepareToRead () {
      System.out.println("prepareToRead Started");     //debug print
      while (numWriters > 0){
         wait(mutex);
      }
      numReaders++;
   }

   private synchronized void doneReading () {
      System.out.println("doneReading Started");     //debug print
      numReaders--;
      //no reader is left in the critical section
      if (numReaders == 0){
         signal(wrt);       //writers can enter
         signal(mutex);     //reader leaves
      }
   }
 
   //public ... someReadMethod () {
   public void someReadMethod () {  
      System.out.println("someReadMethod Started");     //debug print
      prepareToRead();     // reads NOT synchronized => multiple readers

      //<do the reading>
      if (numReaders > 0){
         wait(wrt);            //ensures that not writers enter when there is even one reader
         signal(mutex);        //other readers can enter
      }

      wait(mutex);          //current reader preforms reading here

      doneReading();
   }

//-----------------------

   private void prepareToWrite () {
      System.out.println("prepareToWrite Started");     //debug print
      numWriters++;
      while(numReaders != 0){
         wait(wrt);
      }
   }

   private void doneWriting () {
      System.out.println("doneWriting Started");     //debug print
      numWriters--;
      notify();
   }

   //public synchronized void someWriteMethod (...) {
   public synchronized void someWriteMethod() {
      System.out.println("someWritingMethod Started");     //debug print
      prepareToWrite();      // syncronized => only one writer

      //preforms the write
      //...

      signal(wrt);          //leaves the critcal section

      doneWriting();
   }
}