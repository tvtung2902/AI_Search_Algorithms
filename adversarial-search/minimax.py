class Tree:
    def __init__(self, data, cost = 100000):
        self.data = data
        self.cost = cost # Giá trị mặc định rất lớn
        self.children = [] # Danh sách chứa các nút con
        self.parent = None # Nút cha (mặc định là None)
    
    def add_child(self, child):
        child.parent = self
        self.children.append(child)
        
    def get_data(self):
        return self.data
    
    def get_children(self):
        return self.children
    
    def get_parent(self):
        return self.parent
    
    def __lt__(self, other):
        return self.cost < other.cost
    
# hàm return về max value
def max_value(node):
    if len(node.children) == 0:
        return node # node lá thì return về chính nó
    node.value = -100000
    for child in node.children:
        temp = min_value(child)
        if temp.value > node.value:
            node.value = temp.value
    return node

def min_value(node):
    if len(node.children) == 0:
        return node  # Nếu nút là lá, trả về chính nó
    node.value = 100000  # Giá trị khởi tạo cực đại
    for child in node.children:
        temp = max_value(child)  # Gọi đệ quy hàm MaxValue
        if temp.value < node.value:
            node.value = temp.value  # Cập nhật giá trị nhỏ nhất
    return node

def minimax_search(state):
    max_value(state)

if __name__ == "__main__":
    # Khởi tạo cây tìm kiếm
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
    
    # Xây dựng cây
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
    
    # Chạy thuật toán Minimax
    minimax_search(A)
    
    # In giá trị của nút gốc sau khi tìm kiếm
    print("Root value after Minimax search:", A.value)