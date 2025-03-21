import heapq # hàng đợi ưu tiên

# Định nghĩa lớp TreeNode để biểu diễn các nút trong cây tìm kiếm
class TreeNode:
    def __init__(self, data, goal_cost):
        self.data = data   
        self.goal_cost = goal_cost
        self.children = []
    def add_child(self, child):
        self.children.append(child)
    def get_children(self):
        return self.children 

# Cập nhật frontier nếu có một nút tốt hơn tồn tại
def update_frontier(frontier, new_node):
    for idx, node in enumerate(frontier):
        if node.data == new_node.data: # Kiểm tra nếu nút đã tồn tại trong frontier
            if frontier[idx].goal_cost > new_node.goal_cost: # Nếu chi phí nhỏ hơn, cập nhật
                frontier[idx] = new_node
            return
    frontier.append(new_node)  # Nếu nút chưa tồn tại, thêm vào frontie
   
# Thuật toán tìm kiếm tốt nhất trước (GBFS)
def GBF_search(initial_state, goal_state):
    frontier = []  # Hàng đợi ưu tiên (open list)
    explored = []  # Danh sách các nút đã mở rộng (closed list)
    heapq.heappush(frontier, (initial_state.goal_cost, initial_state))  # Đưa nút gốc vào frontier
    while frontier:
        _, state = heapq.heappop(frontier)  # Lấy nút có giá trị heuristic thấp nhất
        explored.append(state)  # Đánh dấu nút đã thăm
        if state.data == goal_state.data:  # Kiểm tra nếu tìm thấy đích
            return explored # Trả về danh sách nút đã thăm
        for neighbor in state.get_children():  # Duyệt qua các nút con
            if neighbor not in frontier and neighbor not in explored:
                heapq.heappush(frontier, (neighbor.goal_cost, neighbor))  # Thêm vào frontier
            elif neighbor in frontier:
                update_frontier(frontier, neighbor)  # Cập nhật nếu tìm thấy nút tốt hơn
    return False  # Không tìm thấy đường đi
        
# Chạy chương trình
if __name__ == "__main__":
    # Khởi tạo các nút với tên và chi phí heuristic
    A = TreeNode("A", 6)
    B = TreeNode("B", 3)
    C = TreeNode("C", 4)
    D = TreeNode("D", 5)
    E = TreeNode("E", 3)
    F = TreeNode("F", 1)
    G = TreeNode("G", 6)
    H = TreeNode("H", 2)
    I = TreeNode("I", 5)
    J = TreeNode("J", 4)
    K = TreeNode("K", 2)
    L = TreeNode("L", 0)  # Đích
    M = TreeNode("M", 4)
    N = TreeNode("N", 0)
    O = TreeNode("O", 4)

    # Xây dựng cây bằng cách thiết lập các quan hệ cha - con
    A.add_child(B)
    A.add_child(C)
    A.add_child(D)
    B.add_child(E)
    B.add_child(F)
    C.add_child(G)
    C.add_child(H)
    D.add_child(I)
    D.add_child(J)
    E.add_child(K)
    F.add_child(L)
    H.add_child(M)
    H.add_child(N)

    # Chạy thuật toán tìm kiếm
    result = GBF_search(A, L)
    
    # Hiển thị kết quả
    if result:
        path = "Explored: " + " -> ".join(node.data for node in result)
        print(path)
    else:
        print("404 Not Found!")