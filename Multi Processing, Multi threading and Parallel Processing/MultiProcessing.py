import multiprocessing
import requests
import time
def send_request(url):
    response = requests.get(url)
    return response.status_code

if __name__ == "__main__":
 

    start_time = time.time()
    
    urls = ["https://jovian.com/"] * 500

    pool = multiprocessing.Pool()

    result = pool.map(send_request,urls)
    # send_request("https://jovian.com/")
    # de
    pool.close()
    pool.join()

    print(result)

    print(time.time() - start_time, "seconds")
