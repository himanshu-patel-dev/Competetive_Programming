""" do not keep file name as queue.py else it will import same file as module """
from queue import Queue
q = Queue()
q.put(1)
q.put(2)
print(q)
print("Size of q: ",q.qsize())
print("Front element of q: ",q.get())
print("Check if q is empty: ",q.empty())
