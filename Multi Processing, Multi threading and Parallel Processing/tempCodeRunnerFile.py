# Python program to illustrate the concept
# of threading
# importing the threading module
import threading
import requests
import os
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
    t1.start()
	# starting thread 2
    t2.start()

	# wait until thread 1 is completely executed
    t1.join()
	# wait until thread 2 is completely executed
    t2.join()

	# both threads completely executed
    print("Done!")
