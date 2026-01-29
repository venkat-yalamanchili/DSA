from collections import deque

custQueue = deque(maxlen=5)
print(custQueue)

custQueue.append(1)
custQueue.append(1)
custQueue.append(1)
custQueue.append(1)
print(custQueue)