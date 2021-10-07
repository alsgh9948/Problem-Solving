from sys import stdin

class Node(object):
    def __init__(self,name,typ):
        self.name=name
        self.type=typ
        self.file_list = set()
        self.folder_list = []

input = stdin.readline
n,m = map(int, input().split())

folders = {}
for _ in range(n+m):
    up,name,typ = input().strip().split()
    if up not in folders:
        node = Node(up,'1')
        folders[up] = node

    if typ == '0':
        folders[up].file_list.add(name)
    else:
        if name not in folders:
            node = Node(name, '1')
            folders[name] = node
        folders[up].folder_list.append(folders[name])

def solv():
    k = int(input())
    for _ in range(k):
        paths = input().strip().split()
        src = paths[0].split('/')[-1]
        dest = paths[1].split('/')[-1]
        move_file(src,dest)

    q = int(input())
    for _ in range(q):
        path = input().strip().split('/')
        files = search_folder(path[-1])
        print(len(set(files)), len(files))

def move_file(src,dest):
    global folders
    for file in folders[src].file_list:
        folders[dest].file_list.add(file)
    folders[src].file_list.clear()

    for folder in folders[src].folder_list:
        folders[dest].folder_list.append(folder)
    folders[src].folder_list.clear()
def search_folder(now):
    files = []
    for next_folder in folders[now].folder_list:
        files += search_folder(next_folder.name)
    files += list(folders[now].file_list)
    return files
solv()