import multiprocessing
import requests 
import time


# The general way to parallelize any operation is to take a particular function that should be run multiple times
#  and make it run parallelly in different processors.

# To do this, you initialize a Pool with n number of processors and 
# pass the function you want to parallelize to one of Pools parallization methods.


def request_get(url):
    response = requests.get(url)
    return response
   
if __name__ == '__main__':
    # multiprocessing.Pool() provides the apply(), map() and starmap() methods to make any function run in parallel
    '''Both apply and map take the function to be parallelized as the main argument.
    But the difference is, apply() takes an args argument that accepts the parameters passed to the ‘function-to-be-parallelized’ as an argument,
    whereas, map can take only one iterable as an argument.'''
    start_time = time.time()

    pool = multiprocessing.Pool()
    pool = multiprocessing.Pool(processes=4)
    inputs = ["https://readersenglish.com/"]*500
    
    ####    By .map()
    # outputs = pool.map(request_get, inputs)
    # pool.close()
    # print("Output: {}".format(outputs))


    ####    By .apply()
    result  = [pool.apply(request_get, args= (u,)) for u in inputs]
    pool.close()
    print(result)
    print(time.time() - start_time, "seconds")

