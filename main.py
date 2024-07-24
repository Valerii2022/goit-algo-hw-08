import heapq

def minimum_cost_to_connect_cables(cable_lengths):
    heapq.heapify(cable_lengths)
    
    total_cost = 0
    
    while len(cable_lengths) > 1:
        first = heapq.heappop(cable_lengths)
        second = heapq.heappop(cable_lengths)
        
        cost = first + second
        total_cost += cost
        
        heapq.heappush(cable_lengths, cost)
    
    return total_cost

# Тестування
cables = [4, 3, 2, 6]
print(f"Мінімальні витрати на з'єднання: {minimum_cost_to_connect_cables(cables)}")
