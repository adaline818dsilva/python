import heapq
# List of elements
elements = [20, 40, 30, 1, 3, 6, 2, 5, 36]

# Create a max-heap by pushing negative values
max_heap = []
for i in elements:
    heapq.heappush(max_heap, -i)

# Extract elements from the heap in descending order
sorted_desc = [-heapq.heappop(max_heap) for _ in range(len(max_heap))]
print("Elements in descending order:", sorted_desc)


