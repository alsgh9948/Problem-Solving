from sys import stdin

input = stdin.readline
class Node:
    def __init__(self, alpha):
        self.alpha = alpha
        self.child = []
        self.no_remove_flag = False
        self.target_flag = False

tc = int(input())

def solv():
    global answer
    answer = 0
    n, files, m, no_remove_files = input_data()

    if m == 0:
        print(1)
    else:
        tri = make_tri(files)
        set_no_remove_file(no_remove_files,tri)

        remove_file(tri)
        print(answer)
def remove_file(now):
    global answer
    if now.no_remove_flag or now.alpha == '-':
        if now.target_flag:
            answer += 1

        for child in now.child:
            remove_file(child)
    else:
        answer += 1
def set_no_remove_file(no_remove_files,tri):

    for file in no_remove_files:
        now = tri
        for alpha in file:
            now = search_child(now,alpha)
            if not now:
                break
            else:
                now.no_remove_flag = True
def make_tri(files):
    tri = Node('-')

    for file in files:
        now = tri
        for alpha in file:
            temp = search_child(now,alpha)
            if not temp:
                new_node = Node(alpha)
                now.child.append(new_node)
                now = new_node
            else:
                now = temp
        now.target_flag = True
    return tri

def search_child(now,alpha):
    for child in now.child:
        if child.alpha == alpha:
            return child
    return None

def input_data():
    n = int(input())
    files = [input().strip() for _ in range(n)]

    m = int(input())
    no_remove_files = [input().strip() for _ in range(m)]

    return n,files,m,no_remove_files
for _ in range(tc):
    solv()