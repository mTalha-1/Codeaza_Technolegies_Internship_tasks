# Python program to illustrate the concept
# of threading
# importing the threading module
import threading
import requests
import os
import time
def get_status(response):
    print("Task 1 assigned to thread: {}".format(threading.current_thread().name))
    print("ID of process running task 1: {}".format(os.getpid()))   
    print(response.status_code)



def send_request(url):
    print("Task 2 assigned to thread: {}".format(threading.current_thread().name))
    print("ID of process running task 2: {}".format(os.getpid()))
    response = requests.get(url)
    return response


if __name__ =="__main__":
    print("ID of process running main program: {}".format(os.getpid()))
    # print name of main thread
    print("Main thread name: {}".format(threading.current_thread().name))

	# creating thread
    url = 'https://dribbble.com/tags/cofee'
    t1 = threading.Thread(target=send_request, args=(url,))
    t2 = threading.Thread(target=get_status, args=(send_request(url),))
	# starting thread 1 
    start_time_thread1 = time.perf_counter()
    t1.start()
	# starting thread 2
    start_time_thread2 = time.perf_counter()
    t2.start()

	# wait until thread 1 is completely executed
    t1.join()
    end_time_thread1 = time.perf_counter()
    execution_time_t1 = end_time_thread1 - start_time_thread1
    # wait until thread 2 is completely executed
    t2.join()
    end_time_thread2 = time.perf_counter()
    execution_time_t2 = end_time_thread2 - start_time_thread2


	# both threads completely executed
    print('Execution_time of t1: ',execution_time_t1)
    print('Execution_time of t2: ',execution_time_t2)
    print("Done!")
