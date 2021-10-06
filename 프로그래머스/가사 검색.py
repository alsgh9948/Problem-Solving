from sys import setrecursionlimit
setrecursionlimit(100001)
def solution(words, queries):
    answer = []
    trie = make_trie(words, {'length': {}, 'child': {}})

    r_words = []
    all_wild = {}
    for word in words:
        r_words.append(word[::-1])
        length = len(word)
        if length in all_wild:
            all_wild[length] += 1
        else:
            all_wild[length] = 1
    r_trie = make_trie(r_words, {'length': {}, 'child': {}})

    for q in queries:
        if q[0] == q[-1] == '?':
            answer.append(all_wild.get(len(q),0))
        elif q[0] == '?':
            answer.append(search_trie(q[::-1],0,r_trie))
        else:
            answer.append(search_trie(q,0,trie))
    return answer


def make_trie(words, trie):
    for word in words:
        cur = trie
        length = len(word)
        for w in word:
            if w in cur['child']:
                cur = cur['child'][w]
                if length in cur['length']:
                    cur['length'][length] += 1
                else:
                    cur['length'][length] = 1
            else:
                cur['child'][w] = {
                    'length': {
                        length: 1
                    },
                    'child': {}
                }
                cur = cur['child'][w]
    return trie
def search_trie(q,idx,trie):
    if q[idx] == '?':
        return trie['length'].get(len(q),0)
    else:
        if q[idx] in trie['child']:
            return search_trie(q,idx+1,trie['child'][q[idx]])
        else:
            return 0
a = ["frodo", "front", "frost", "frozen", "frame", "a"]
b = ["fro??", "????o", "fr??", "fro???", "pro?","??"]
print(solution(a,b))