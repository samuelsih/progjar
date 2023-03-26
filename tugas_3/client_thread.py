from threading import Thread
from counter import AtomicCounter
from task import kirim_data
import sys

def client_thread():
    threads = []
    
    try:
        count = AtomicCounter()
        
        for i in range(sys.maxsize):
            threads.append(Thread(target=kirim_data))
            count.increment()
            threads[i].start()

        for thread in threads:
            thread.join()
    except Exception:
        print("limit reached")
    finally:
        print(f"Total: {count.value() - 1}")



if __name__ == "__main__":
    client_thread()