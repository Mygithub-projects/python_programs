from collections import deque
queue = deque(["Eric","John",",michael"])
queue.append("Terry")           # Terry arrives
queue.append("Graham")          # Graham arrives
queue.popleft()                 # The first to arrive now leaves
print("first removal", queue)
queue.popleft()                 # The second to arrive now leaves
print("second removal" ,queue)                         # Remaining queue in order of arrival

