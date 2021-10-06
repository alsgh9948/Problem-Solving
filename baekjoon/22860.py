from sys import stdin

class Node(object):
    def __init__(self,name,typ):
        self.name=name
        self.type=typ
        self.file_list = []
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
        folders[up].file_list.append(name)
    else:
        if name not in folders:
            node = Node(name, '1')
            folders[name] = node
        folders[up].folder_list.append(folders[name])

def solv():
    q = int(input())
    for _ in range(q):
        path = input().strip().split('/')
        files = search_folder(path[-1])
        print(len(set(files)), len(files))
def search_folder(now):
    files = []
    for next_folder in folders[now].folder_list:
        files += search_folder(next_folder.name)
    files += folders[now].file_list
    return files
solv()