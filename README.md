AI Search Algorithms

This repository contains implementations of various AI search algorithms, categorized into uninformed (blind) search, informed (heuristic-based) search, and adversarial search.

📌 Algorithms Included

🔍 Uninformed Search (Blind Search)

Breadth-First Search (BFS) – Explores all nodes at the present depth before moving to the next depth level.

Depth-First Search (DFS) – Explores as far as possible along each branch before backtracking.

Uniform Cost Search (UCS) – Expands the least-cost node first, ensuring the optimal path is found.

🤖 Informed Search (Heuristic-Based)

Greedy Best-First Search – Expands the node with the lowest heuristic value, aiming to reach the goal quickly.

A Search* – Combines UCS and Greedy BFS using the formula: f(n) = g(n) + h(n), ensuring optimality and efficiency.

🎭 Adversarial Search (Game AI)

Minimax Algorithm – A decision-making algorithm used in two-player games, assuming both players play optimally.

Alpha-Beta Pruning – An optimization of Minimax that reduces the number of nodes evaluated, improving efficiency.

📂 Repository Structure

⚙️ How to Run

Ensure you have Python installed. Clone the repository and run any script:

📚 References

"Artificial Intelligence: A Modern Approach" by Stuart Russell and Peter Norvig

🤝 Contributing

Feel free to open issues or submit pull requests if you have improvements or additional algorithms to contribute!

