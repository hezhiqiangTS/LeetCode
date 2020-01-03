import heapq

heap = []
data = [1, 3, 5, 7, 9, 2, 4, 6, 8, 10]
for i in data:
    heapq.heappush(heap, i)
    
print(heap)

lis = []
while heap:
    lis.append(heapq.heappop(heap))
print(lis)

heapq.heapify(data)
print(data)
