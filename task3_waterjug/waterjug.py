# DFS, BFS
from collections import deque

def waterJugProblem(capacity1, capacity2, goal):
    queue = deque()
    visited = set()

    queue.append((0, 0,'Both empty'))
    visited.add((0, 0,'Both empty'))

    actions = []

    while queue:
        jug1, jug2,rule = queue.popleft()
        actions.append((jug1, jug2,rule))

        # Check if target is achieved
        if jug1 == goal or jug2 == goal:
            print("Solution Found")
            for action in actions:
                print(action)
            return True

        # Apply rules
        rules = [#                             
           (capacity1, jug2,'Fill jug1') ,   
           (jug1, capacity2,'Fill jug2'),   
           (0, jug2,'Empty jug1'),            
           (jug1, 0,'Empty jug2'),           
           (capacity1, abs(capacity2-(capacity1-(capacity2-jug1))),'Pour from jug2 to jug1'),
           (abs(capacity1-(capacity2-(capacity1-jug2))), capacity2,'Pour from jug1 to jug2'), 
           (jug1+jug2, 0,'Pour jug1 into jug2 until jug1 is empty'), 
           (0, jug1+jug2,'Pour jug2 into jug1 until jug2 is empty'), 
        ] 

        for state in rules:
            if state not in visited:
                visited.add(state)
                queue.append(state)

    print("No Solution found")
    return False

jug1Capacity = 4
jug2Capacity = 3
target = 2          

waterJugProblem(jug1Capacity, jug2Capacity, target)