#!/usr/bin/env python
# _*_ coding: utf-8 _*_
# @Project: New_Health
# @Date: 11/6/2018
# @Author: MatthewP

from multiprocessing import Process, Queue

sentinel = -1

def creator(data, q):
    print('creating data and putting in on the queue')
    for item in data:
        print('Adding {}'.format(item))
        q.put(item)

def my_consumer(q):
    while True:
        data = q.get()
        print('data found to be processed: {}'.format(data))
        processed = data*2
        print(processed)

        if data is sentinel:
            break

if __name__ == '__main__':
    q = Queue()
    data = [5, 10, 13, -1]
    process_one = Process(target=creator, args=(data, q))
    process_two = Process(target=my_consumer, args=(q,))
    process_one.start()
    process_two.start()

    q.close()
    q.join_thread()

    process_one.join()
    process_two.join()