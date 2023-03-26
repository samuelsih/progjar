from concurrent.futures import ThreadPoolExecutor, as_completed
from counter import AtomicCounter
from task import kirim_data
import datetime

maxsize = 2044

def threadpool_client():
    counter = AtomicCounter()
    
    with ThreadPoolExecutor() as pool:
        start = datetime.datetime.now()
        
        futures = [pool.submit(kirim_data) for i in range(maxsize)]
                
        for future in as_completed(futures):
            future.result()
            counter.increment()
            
        end  = datetime.datetime.now() - start
        print(f"Request total {counter.value()}")
        print(f"Waktu TOTAL yang dibutuhkan {end} detik {start}")
        
if __name__ == "__main__":
    threadpool_client()
