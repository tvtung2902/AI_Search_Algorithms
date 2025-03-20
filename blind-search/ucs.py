import heapq

def uniform_cost_search(graph, start, goal):
    frontier = []  # Hàng đợi ưu tiên (ưu tiên chi phí thấp nhất)
    heapq.heappush(frontier, (0, start, [start]))  # (chi phí, nút hiện tại, đường đi)
    explored = set()
    
    while frontier:
        cost, node, path = heapq.heappop(frontier)
        
        if node in explored:
            continue
                
        explored.add(node)
        
        if node == goal:
            return cost, path  # Trả về chi phí và đường đi tối ưu
        
        for neighbor, weight in graph.get(node, []):
            if neighbor not in explored:
                heapq.heappush(frontier, (cost + weight, neighbor, path + [neighbor]))
    
    return float("inf"), []  # Không tìm thấy đường đi

# Định nghĩa đồ thị dạng danh sách kề
graph = {
    "Hà Nội": [("Nam Định", 95), ("Phú Lý", 60)],
    "Nam Định": [("Thanh Hóa", 95), ("Hà Nội", 95)],
    "Phú Lý": [("Ninh Bình", 40), ("Hà Nội", 60)],
    "Thanh Hóa": [("Ninh Bình", 64), ("Nam Định", 95)],
    "Ninh Bình": [("Thanh Hóa", 64), ("Phú Lý", 40)]
}

start = "Hà Nội"
goal = "Thanh Hóa"

cost, path = uniform_cost_search(graph, start, goal)
print(f"Chi phí tối ưu: {cost}")
print(f"Đường đi tối ưu: {' -> '.join(path)}")