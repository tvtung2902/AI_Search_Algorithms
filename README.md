# AI Search Algorithms

📌 **Giới thiệu**  
Repo này chứa các thuật toán tìm kiếm trong trí tuệ nhân tạo (AI), bao gồm cả tìm kiếm mù, tìm kiếm có thông tin, và tìm kiếm có đối thủ.

## 🏗 Cấu trúc repo
```
📂 ai-search-algorithms
│── 📂 blind-search/          # Thuật toán tìm kiếm mù
│    ├── bfs.py              # Tìm kiếm theo chiều rộng (BFS)
│    ├── dfs.py              # Tìm kiếm theo chiều sâu (DFS)
│    ├── ucs.py              # Tìm kiếm chi phí đồng nhất (UCS)
│
│── 📂 informed-search/       # Thuật toán tìm kiếm có thông tin
│    ├── greedy-bfs.py       # Tìm kiếm tham lam (Greedy BFS)
│    ├── a-star.py           # Tìm kiếm A*
│
│── 📂 adversarial-search/    # Thuật toán tìm kiếm có đối thủ
│    ├── minimax.py          # Thuật toán Minimax
│    ├── alpha-beta.py       # Cắt tỉa Alpha-Beta
│
│── README.md                # Hướng dẫn sử dụng
```

---

## 🔍 Thuật toán tìm kiếm mù (Blind Search)
Không sử dụng thông tin về đích, chỉ mở rộng các nút một cách có hệ thống.

- **BFS (Breadth-First Search)**: Tìm kiếm theo chiều rộng, duyệt từng tầng trước.
- **DFS (Depth-First Search)**: Tìm kiếm theo chiều sâu, đi sâu vào một nhánh trước.
- **UCS (Uniform-Cost Search)**: Tìm kiếm chi phí đồng nhất, mở rộng nút có chi phí thấp nhất.

## 💡 Thuật toán tìm kiếm có thông tin (Informed Search)
Sử dụng thông tin ước lượng để dẫn hướng tìm kiếm.

- **Greedy BFS**: Chọn nút có giá trị hàm heuristic nhỏ nhất.
- **A***: Kết hợp chi phí thực tế và heuristic để tìm đường tối ưu.

## 🎭 Thuật toán tìm kiếm có đối thủ (Adversarial Search)
Dùng trong trò chơi đối kháng (game AI).

- **Minimax**: Duyệt cây trò chơi để tìm nước đi tốt nhất.
- **Alpha-Beta Pruning**: Cải tiến Minimax để cắt tỉa những nhánh không cần thiết.

---

## 🚀 Cách chạy các thuật toán

Cài đặt Python nếu chưa có:
```
pip install -r requirements.txt
```
Chạy từng thuật toán bằng lệnh:
```
python blind-search/bfs.py
python informed-search/a-star.py
python adversarial-search/minimax.py
```

---

## 📌 Đóng góp
Bạn có thể đóng góp bằng cách tạo một **pull request** hoặc mở **issue**.

🌟 **Star repo nếu bạn thấy hữu ích!**

