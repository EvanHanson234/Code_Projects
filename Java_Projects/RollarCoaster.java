/*	
	Rollar Coaster Problem
	Written by Evan Hanson
	December 1st, 2022		
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
*/