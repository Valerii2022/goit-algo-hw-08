
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
cables_1 = [7, 10, 3, 5, 1]
print(f"Мінімальні витрати на з'єднання cables_1: {minimum_cost_to_connect_cables(cables_1)}")
cables_2 = [2, 9, 7, 3, 12, 8]
print(f"Мінімальні витрати на з'єднання cables_2: {minimum_cost_to_connect_cables(cables_2)}")
cables_3 = [1, 15, 4, 3, 5, 20, 24, 7]
print(f"Мінімальні витрати на з'єднання cables_3: {minimum_cost_to_connect_cables(cables_3)}")