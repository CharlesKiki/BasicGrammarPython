	#!.usr/bin/env python
	import threading 
	from time import sleep, ctime
	loops = [4,2]

	def loop(nloop,nsec):
		print ('start loop',nloop, 'at:' , ctime())
		sleep(nesc)
		print ('loop',nloop,'done at:', ctime())
	def main():
		print ('starting at:' , ctime())
		threads[]
		
		for i in nloops:
			t = threading.Thread(target = loop,args = (i,loops[i]))
			#target is what the function you want to run in thread
			#args is parameter send to target 
			thread.append(t)
			#add thread
		for i in nloops:	#start thread
			threads[i].start()
			
		for i in nloops:	#wait for all
			thread[i].join()	#threads to finish 
		
		print ('all DONE at:' , ctime())
		
	if __name__ == '__main__':
		main()