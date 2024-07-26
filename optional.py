import heapq

def merge_k_lists(lists):
    min_heap = []
    for i, lst in enumerate(lists):
        if lst:
            heapq.heappush(min_heap, (lst[0], i, 0))
    
    result = []
    
    while min_heap:
        val, list_index, element_index = heapq.heappop(min_heap)
        result.append(val)
        
        if element_index + 1 < len(lists[list_index]):
            next_val = lists[list_index][element_index + 1]
            heapq.heappush(min_heap, (next_val, list_index, element_index + 1))
    
    return result

# Тестування
lists = [[1, 4, 5], [1, 3, 4], [2, 6]]
merged_list = merge_k_lists(lists)
print("Відсортований список:", merged_list)
lists_2 = [[1, 3, 4, 7, 9], [1, 2, 6, 8, 10], [2, 6, 7, 9]]
merged_list_2 = merge_k_lists(lists_2)
print("Відсортований список:", merged_list_2)

