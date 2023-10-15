import os
import logging
import time

def test_concurrent_requests():
    urls = {
        'url1': '127.0.0.1:5000/thread',
        'url2': '127.0.0.1:5000/'
    }
    st_time = time.time()
    cmd = "curl {} ".format(urls["url1"])
    res = os.system(cmd)
    end_time = time.time()
    time_elapsed = round(end_time - st_time, 4)
    st_time = time.time()
    request_count = 500
    con_cmd = '& '.join([cmd for i in range(request_count)])
    con_res = os.system(con_cmd)
    end_time = time.time()
    con_time_elapsed = round(end_time - st_time, 4)
    print(time_elapsed)
    print(con_time_elapsed)
    concurrency_rate = (con_time_elapsed/time_elapsed) 
    logging.info("Concurrency Rate : {}".format(concurrency_rate))
    assert concurrency_rate > 2