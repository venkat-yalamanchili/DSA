import queue as q

custQueue = q.Queue(maxsize=3)
custQueue.put(1)
custQueue.put(2)
custQueue.put(3)
print(custQueue.full())
print(custQueue.empty())
print(custQueue.qsize())

custQueue.get()
print(custQueue.full())
print(custQueue.empty())
print(custQueue.qsize())
