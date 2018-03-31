import logging
import threading
import time
import queue
import random

put_interval = 2
num_worker_put_threads = 3
num_worker_get_threads = 2

def worker_put(cnt, t):
    cnt.value = random.randint(1,9)
    thread_id = str(threading.get_ident())
    while True:
        cnt.value = cnt.value + 1
        q.put(cnt.value)
        print("id=" + thread_id + " put item: " + str(cnt.value))
        time.sleep(t)

def worker_get():
    thread_id = str(threading.get_ident())
    while True:
        item = q.get()
        print("id=" + thread_id + " get item: " + str(item))

q = queue.Queue()

threads = []
local_data = threading.local()

for i in range(num_worker_put_threads):
    sleep = i + 1
    t = threading.Thread(target=worker_put, args=(local_data, put_interval))
    t.start()
    threads.append(t)

for i in range(num_worker_get_threads):
    t = threading.Thread(target=worker_get)
    t.start()
    threads.append(t)

for t in threads:
    t.join()
print("end")
