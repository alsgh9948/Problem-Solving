from sys import stdin

input = stdin.readline
dx = [-1,1,0,0,-1,1,-1,1]
dy = [0,0,-1,1,-1,-1,1,1]

w = int(input())
word_dictionary = []
for _ in range(w):
    word_dictionary.append(input().strip())
input()

def solv():
    tri = make_tri()

    b = int(input())
    for _ in range(b):
        board = [list(input().strip()) for _ in range(4)]
        search_result = set()
        visited = [[False]*4 for _ in range(4)]
        for x in range(4):
            for y in range(4):
                now = tri
                for child in now.child:
                    if board[x][y] == child.alpha:
                        if child.is_end:
                            search_result.add(board[x][y])
                        visited[x][y] = True
                        search_word(child,x,y,board,board[x][y],search_result,visited)
                        visited[x][y] = False
                        break
        input()
        score = 0
        long_word = ''
        words = sorted(search_result)
        for word in words:
            if len(long_word) < len(word):
                long_word = word
            score += calc_score(word)
        print(score, long_word, len(words))
class Node(object):
    def __init__(self,alpha=''):
        self.alpha = alpha
        self.child = []
        self.is_end = False
def make_tri():
    tri = Node()

    for word in word_dictionary:
        now = tri
        for alpha in word:
            flag = False
            for child in now.child:
                if child.alpha == alpha:
                    now = child
                    flag = True
                    break
            if not flag:
                child = Node(alpha)
                now.child.append(child)
                now = child
        now.is_end = True
    return tri

def search_word(now,x,y,board,word,search_result,visited):
    if now.is_end:
        search_result.add(word)

    if len(word) == 8:
        return

    for d in range(8):
        nx = x + dx[d]
        ny = y + dy[d]

        if point_validator(nx,ny,visited):
            alpha = board[nx][ny]
            for child in now.child:
                if child.alpha == alpha:
                    visited[nx][ny] = True
                    search_word(child,nx,ny,board,word+board[nx][ny],search_result,visited)
                    visited[nx][ny] = False
def point_validator(x,y,visited):
    if x < 0 or y < 0 or x >= 4 or y >= 4:
        return False
    elif visited[x][y]:
        return False
    return True

def calc_score(word):
    word_lenght = len(word)
    if word_lenght == 8:
        return 11
    elif word_lenght == 7:
        return 5
    elif word_lenght == 6:
        return 3
    elif word_lenght == 5:
        return 2
    elif word_lenght in [3,4]:
        return 1
    else:
        return 0
solv()