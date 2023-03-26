from multiprocessing import Process
from counter import AtomicCounter
from task import kirim_data
import datetime

maxsize = 2044

def client_process():
    start = datetime.datetime.now()
    counter = AtomicCounter()
    
    for i in range(maxsize):
        global count
        
        processor = Process(target=kirim_data)
        processor.start()
        processor.join()
        
        counter.increment()
        
    end  = datetime.datetime.now() - start
    
    print(f"Request total {count.value()}")
    print(f"Waktu TOTAL yang dibutuhkan {end} detik {start}")

if __name__ == "__main__":
    client_process()