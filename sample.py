import gevent.monkey
gevent.monkey.patch_socket()

import gevent
import requests
import json

def fetch(pid):
    datetime = json.loads(requests.get('http://json-time.appspot.com/time.json').text)['datetime']
    print(pid,datetime)
    return datetime

def synchronous():
    for i in range(1,10):
        fetch(i)

def asynchronous():
    threads = []
    for i in range(1,10):
        threads.append(gevent.spawn(fetch, i))
    gevent.joinall(threads)

print('Synchronous:')
synchronous()

print('Asynchronous:')
asynchronous()