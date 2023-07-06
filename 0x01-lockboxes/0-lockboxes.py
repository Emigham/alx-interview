from collections import deque

def canUnlockAll(boxes):
    n = len(boxes)  # Total number of boxes
    visited = [False] * n  # Track visited boxes
    visited[0] = True  # Mark the first box as visited
    queue = deque([0])  # Start BFS from the first box

    while queue:
        box = queue.popleft()
        for key in boxes[box]:
            if not visited[key]:
                visited[key] = True
                queue.append(key)

    return all(visited)

