from threading import Thread
from counter import AtomicCounter
from task import kirim_data
import sys
import datetime

maxsize = 2044

def client_thread():
    start = datetime.datetime.now()
    counter = AtomicCounter()
    
    for i in range(maxsize):
        thread = Thread(target=kirim_data)
        counter.increment()
        thread.start()
        thread.join()
    
    end  = datetime.datetime.now() - start
    print(f"Request total {counter.value()}")
    print(f"Waktu TOTAL yang dibutuhkan {end} detik {start}")



if __name__ == "__main__":
    client_thread()