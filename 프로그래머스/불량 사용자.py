class Node:
    def __init__(self, alpha):
        self.alpha = alpha
        self.count = 0
        self.child = []
        self.is_end = False

def solution(user_id, banned_id):
    global answer,visited,word_info
    answer = 0
    visited = set()
    word_info = {}
    tri = make_tri(user_id)

    candidates = []
    for id in banned_id:
        candidates.append(sorted(check_banned(id, 0, tri, '', [])))

    print(candidates)
    select_user(candidates,0,'')
    return answer

def select_user(candidates,now,select):
    global answer, word_info, visited
    if now == len(candidates):
        tmp = ''.join(sorted(select))
        if tmp not in visited:
            answer += 1
            visited.add(tmp)
        return

    for id in candidates[now]:
        if not word_info[id][0]:
            word_info[id][0] = True
            select_user(candidates,now+1,select+word_info[id][1])
            word_info[id][0] = False

def check_banned(id, idx, now, word, candidate):
    global word_info
    if idx == len(id):
        if now.is_end:
            candidate.append(word)
            if word not in word_info:
                word_info[word] = [False,str(len(word_info))]
        return candidate

    if id[idx] == '*':
        for child in now.child:
            candidate = check_banned(id, idx + 1, child, word+child.alpha, candidate)
    else:
        for child in now.child:
            if child.alpha == id[idx]:
                candidate = check_banned(id, idx + 1, child, word+child.alpha, candidate)
    return candidate
def make_tri(user_id):
    tri = Node('-')

    for id in user_id:
        now = tri
        for alpha in id:
            now = search_child(now, alpha)
        now.is_end = True
    return tri

def search_child(now, alpha):
    for child in now.child:
        if child.alpha == alpha:
            now.count += 1
            return child
    node = Node(alpha)
    node.count += 1
    now.child.append(node)
    return node

a = ["frodo", "fradi", "crodo", "abc123", "frodoc"]
b = ["fr*d*", "*rodo", "******", "******"]
print(solution(a,b))