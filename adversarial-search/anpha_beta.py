class Tree:
    def __init__(self, data, cost=100000, value=None):
        self.data = data 
        self.cost = cost
        self.children = []
        self.parent = None
        self.value = value  # Giá trị của nút, ban đầu là None cho nút trung gian

    def add_child(self, child):
        child.parent = self
        self.children.append(child)

def MaxValue(node, alpha, beta):
    if len(node.children) == 0:  # Nếu là nút lá, trả về chính nó
        return node
    
    node.value = -100000  # Gán giá trị nhỏ nhất ban đầu
    for child in node.children:
        temp = MinValue(child, alpha, beta)  # Gọi MinValue cho con

        if temp.value > node.value:  # Cập nhật giá trị lớn nhất
            node.value = temp.value
        
        if child.value >= beta:  # Cắt tỉa Beta
            return child
        
        if child.value > alpha:  # Cập nhật Alpha
            alpha = child.value

    return node

def MinValue(node, alpha, beta):
    if len(node.children) == 0:  # Nếu là nút lá, trả về chính nó
        return node
    
    node.value = 100000  # Gán giá trị lớn nhất ban đầu
    for child in node.children:
        temp = MaxValue(child, alpha, beta)  # Gọi MaxValue cho con

        if temp.value < node.value:  # Cập nhật giá trị nhỏ nhất
            node.value = temp.value
        
        if child.value <= alpha:  # Cắt tỉa Alpha
            return child
        
        if child.value < beta:  # Cập nhật Beta
            beta = child.value

    return node

def Minimax_Search(state):
    MaxValue(state, -100000, 100000)  # Khởi động thuật toán với Alpha = -∞, Beta = ∞


# ------------------------- Tạo cây -------------------------
if __name__ == "__main__":
    A = Tree("A")
    B = Tree("B")
    C = Tree("C")
    D = Tree("D")
    E = Tree("E")
    F = Tree("F")
    G = Tree("G")
    H = Tree("H")
    I = Tree("I")
    J = Tree("J")
    K = Tree("K")
    L = Tree("L")
    M = Tree("M")
    N = Tree("N")
    Z = Tree("Z")

    A.add_child(B)
    A.add_child(C)
    B.add_child(D)
    B.add_child(E)
    C.add_child(F)
    C.add_child(G)
    D.add_child(H)
    D.add_child(I)
    E.add_child(J)
    E.add_child(K)
    F.add_child(M)
    F.add_child(N)
    G.add_child(L)
    G.add_child(Z)

    # Gán giá trị cho các nút lá
    H.value = 2
    I.value = 9
    J.value = 7
    K.value = 4
    M.value = 8
    N.value = 9
    L.value = 3
    Z.value = 5

    # Thực hiện thuật toán Minimax với cắt tỉa Alpha-Beta
    Minimax_Search(A)
    print("Giá trị Minimax của gốc A:", A.value)
