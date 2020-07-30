import sys
import threading

def fillDepth(parent, i, depth):
    
    if depth[i] != 0:
        return

    if parent[i] == -1:
        depth[i] = 1
        return
    
    if depth[parent[i]] == 0 :
        fillDepth(parent, parent[i], depth)

    depth[i] = depth[parent[i]] + 1



def compute_height(n, parent):
    
    depth = [0 for i in range(n)]

    for i in range(n):
        fillDepth(parent, i, depth)

    return max(depth)
    
    # max_height = 0
    # for vertex in range(n):
    #     height = 0
    #     current = vertex
    #     while current != -1:
    #         height += 1
    #         current = parents[current]
    #     max_height = max(max_height, height)
    # return max_height


def main():
    n = int(input())
    parents = list(map(int, input().split()))
    print(compute_height(n, parents))


# In Python, the default limit on recursion depth is rather low,
# so raise it here for this problem. Note that to take advantage
# of bigger stack, we have to launch the computation in a new thread.
sys.setrecursionlimit(10**7)  # max depth of recursion
threading.stack_size(2**27)   # new thread will get stack of such size
threading.Thread(target=main).start()
