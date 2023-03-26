from concurrent.futures import ThreadPoolExecutor, as_completed
from counter import AtomicCounter
from task import kirim_data
import sys

def threadpool_client():
    counter = AtomicCounter()
    
    try:
        with ThreadPoolExecutor() as pool:
            futures = [pool.submit(kirim_data) for i in range(sys.maxsize)]
                
        for future in as_completed(futures):
            future.result()
            counter.increment()                
    except Exception as e:
        print("error: ", e)
    finally:
        print(f"Total: {counter.value()}")
        
if __name__ == "__main__":
    threadpool_client()