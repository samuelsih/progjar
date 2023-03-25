from multiprocessing import Process
from counter import AtomicCounter
from task import kirim_data
import sys

count = AtomicCounter()

def client_process():
    processes = []

    for i in range(sys.maxsize):
        processes.append(Process(target=kirim_data))
        count.increment()
        processes[i].start()

    for process in processes:
        process.join()

if __name__ == "__main__":
    client_process()
    print(count.value)