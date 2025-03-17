1. Không gian trạng thái (State Space)
   - Tập hợp tất cả các trạng thái có thể có của bài toán.
   - Ví dụ: Trong bài toán mê cung, mỗi vị trí trong mê cung là một trạng thái có thể có.

2. Trạng thái ban đầu (Initial State)
   - Trạng thái bắt đầu của bài toán.
   - Ví dụ: Trong bài toán tìm đường từ A đến B, trạng thái ban đầu là vị trí A.

3. Trạng thái đích (Goal State)
   - Trạng thái cần tìm để đạt được lời giải.
   - Ví dụ: Trong tìm đường, trạng thái đích là điểm B.

4. Toán tử trạng thái (State Transition Operators)
   - Các phép biến đổi từ một trạng thái sang trạng thái khác.
   - Ví dụ: Trong bài toán 8 puzzle, toán tử là di chuyển ô trống lên, xuống, trái, phải.

5. Tập hợp nghiệm (Solution Space)
   - Tập hợp các trạng thái đích có thể đạt được từ trạng thái ban đầu.
   - Ví dụ: Trong tìm đường, có thể có nhiều con đường khác nhau từ A đến B.

6. Đường đi (Path)
   - Một chuỗi trạng thái liên tiếp từ trạng thái ban đầu đến đích.
   - Ví dụ: Trong một mê cung, đường đi có thể là một chuỗi các bước di chuyển từ lối vào đến lối ra.

7. Chi phí (Cost)
   - Giá trị đánh giá mức độ tối ưu của một đường đi.
   - Ví dụ: Trong tìm đường trên bản đồ, chi phí có thể là tổng khoảng cách đi.

8. Hàm đánh giá (Evaluation Function)
   - Hàm ước lượng độ tốt của một trạng thái.
   - Ví dụ: Trong thuật toán A*, hàm f(n) = g(n) + h(n) ước lượng chi phí đi từ trạng thái hiện tại đến đích.

9. Hàm heuristic (Heuristic Function)
   - Hàm ước lượng chi phí còn lại để đến trạng thái đích.
   - Ví dụ: Trong cờ vua, heuristic có thể là số quân cờ còn lại của đối phương.

10. Mở rộng nút (Node Expansion)
    - Quá trình sinh ra các trạng thái con từ một trạng thái hiện tại.
    - Ví dụ: Trong tìm kiếm BFS, mỗi nút mở rộng sẽ tạo ra các nút con.

11. Tập mở (Open List)
    - Danh sách chứa các trạng thái đang chờ được mở rộng.
    - Ví dụ: Trong A*, Open List chứa các nút chưa được mở rộng nhưng đã được khám phá.

12. Tập đóng (Closed List)
    - Danh sách chứa các trạng thái đã được mở rộng để tránh mở rộng lại.
    - Ví dụ: Trong A*, một nút đã mở rộng sẽ không được thêm lại vào Open List.

13. Cây tìm kiếm (Search Tree)
    - Cấu trúc cây biểu diễn quá trình tìm kiếm từ trạng thái ban đầu đến trạng thái đích.
    - Ví dụ: Trong DFS, cây tìm kiếm có thể sâu và hẹp.

14. Đồ thị tìm kiếm (Search Graph)
    - Cấu trúc đồ thị chứa tất cả các trạng thái có thể có của bài toán.
    - Ví dụ: Trong tìm đường, các nút là các thành phố và các cạnh là con đường nối giữa chúng.

15. Chiến lược tìm kiếm (Search Strategy)
    - Phương pháp tìm kiếm được sử dụng.
    - Ví dụ: Tìm kiếm theo chiều rộng (BFS) hoặc tìm kiếm theo chiều sâu (DFS).

16. Tính đầy đủ (Completeness)
    - Đảm bảo thuật toán có tìm thấy lời giải nếu có.
    - Ví dụ: BFS là thuật toán đầy đủ vì nó luôn tìm ra lời giải nếu có.

17. Tính tối ưu (Optimality)
    - Đảm bảo thuật toán tìm ra lời giải có chi phí nhỏ nhất.
    - Ví dụ: Thuật toán Dijkstra luôn tìm ra đường đi ngắn nhất.

18. Độ phức tạp thời gian (Time Complexity)
    - Lượng thời gian cần thiết để tìm lời giải.
    - Ví dụ: BFS có độ phức tạp O(b^d), với b là số nhánh và d là độ sâu.

19. Độ phức tạp không gian (Space Complexity)
    - Lượng bộ nhớ cần thiết để thực hiện thuật toán.
    - Ví dụ: DFS có độ phức tạp không gian là O(d), với d là độ sâu tối đa của cây tìm kiếm.
