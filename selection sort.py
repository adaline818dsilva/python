def selection_sort(element):
    n = len(element)
    for i in range(n):
        min_idx = i
        for j in range(i+1, n):
            if element[j] < element[min_idx]:
                min_idx = j
        element[i], element[min_idx] = element[min_idx], element[i]
    return element

element = [11,2,3,4,5,7,6,8 ]
res = selection_sort(element)
print(res)
