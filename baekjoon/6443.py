n = int(input())

def solv():
    global input_word,words,visited,used_alpha
    input_word = input().strip()
    visited = [set() for _ in range(len(input_word)+1)]
    used_alpha = [False]*len(input_word)
    words = set()

    select_alpha('')
    answer = sorted(list(words))
    for word in answer:
        print(word)
def select_alpha(word):
    global visited,used_alpha
    if len(word) == len(input_word):
        words.add(word)

    for idx in range(len(input_word)):
        alpha = input_word[idx]
        if not used_alpha[idx]:
            nxt_word = word+alpha
            if nxt_word not in visited[len(nxt_word)]:
                used_alpha[idx] = True
                visited[len(nxt_word)].add(nxt_word)
                select_alpha(nxt_word)
                used_alpha[idx] = False

for _ in range(n):
    solv()