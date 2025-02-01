import sys
import os

# Додаємо шлях до кореневої папки проєкту
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), 'src')))

from task_1_graph_model import create_transport_network, analyze_graph, visualize_graph
from task_2_search_algorithms import dfs_path, bfs_path
from task_3_dijkstra_algorithm import dijkstra_shortest_path

def run_task_1():
    G = create_transport_network()
    analyze_graph(G)
    visualize_graph(G)

def run_task_2():
    G = create_transport_network()
    start, goal = "A", "F"
    print(f"DFS шлях з {start} до {goal}: {dfs_path(G, start, goal)}")
    print(f"BFS шлях з {start} до {goal}: {bfs_path(G, start, goal)}")

def run_task_3():
    G = create_transport_network()
    start, goal = "A", "F"
    path, distance = dijkstra_shortest_path(G, start, goal)
    print(f"Найкоротший шлях з {start} до {goal}: {path} з відстанню {distance}")

def run_tests():
    os.system("python -m unittest discover tests")

def main():
    while True:
        print("\nОберіть опцію:")
        print("1 - Аналіз графа")
        print("2 - Пошук шляхів (DFS, BFS)")
        print("3 - Найкоротший шлях (Дейкстра)")
        print("4 - Запуск тестів")
        print("0 - Вихід")
        choice = input("Введіть номер опції: ")
        
        if choice == "1":
            run_task_1()
        elif choice == "2":
            run_task_2()
        elif choice == "3":
            run_task_3()
        elif choice == "4":
            run_tests()
        elif choice == "0":
            print("Вихід з програми...")
            break
        else:
            print("Невірний вибір, спробуйте ще раз.")

if __name__ == "__main__":
    main()
