import os
import logging
import time

def test_concurrent_requests():
    '''
    Test case to check for the concurrency in the flask application.
    Number of requests can be altered to match the system configurations.
    '''
    urls = {
        'url1': '127.0.0.1:5000/thread',
        'url2': '127.0.0.1:5000/'
    }
    # Single call metric calculation
    st_time = time.time()
    cmd = "curl {} ".format(urls["url1"])   # Command to curl the request to the flask application
    res = os.system(cmd)
    end_time = time.time()
    time_elapsed = round(end_time - st_time, 4)     # Total time elapsed for the single call

    # Concurrent call metric calculation
    st_time = time.time()
    request_count = 500     # Total number of requests to send to the flask application
    con_cmd = '& '.join([cmd for i in range(request_count)])    # Creating curl command to make concurrent requests to the flask application
    con_res = os.system(con_cmd)    # Making the concurrent calls
    end_time = time.time()
    con_time_elapsed = round(end_time - st_time, 4)     # Total time taken for the concurrent requests to go through
    # Printing the respective times
    print("Time taken for single request : ".format(time_elapsed))
    print("Time taken for concurrent {} requests : ".format(request_count, con_time_elapsed))
    con_per_request = (con_time_elapsed/request_count)      # Average time taken by each request in concurrency call
    concurrency_rate = (con_per_request/time_elapsed)      # Rate of concurrent requests getting processed
    logging.info("Concurrency Rate : {}".format(concurrency_rate))
    time_for_serial_calls = time_elapsed * request_count
    threads = time_for_serial_calls / con_time_elapsed
    print("Thread count : {}".format(threads))
    assert threads > 2