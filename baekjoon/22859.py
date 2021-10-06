import sys
html_tag = sys.stdin.readline().strip()

answer = []
def solv():
    idx = 0
    while True:
        start = html_tag[idx:].find('<div title="')
        if start == -1:
            break
        start += idx
        end = idx+html_tag[idx:].find('</div>')+6
        div = html_tag[start:end]

        title_div_end = div.find('">')
        title = div[len('<div title="'):title_div_end].strip()
        p_list = []
        start_p = title_div_end+2
        while True:
            tmp = start_p+3
            start_p = div[start_p:].find('<p>')
            if start_p == -1:
                break
            start_p += tmp
            end_p = div[start_p:].find('</p>')
            p = ''
            flag = False
            for c in div[start_p:start_p+end_p]:
                if c == '<':
                    flag = True
                elif flag and c == '>':
                    flag = False
                elif not flag:
                    p += c
            while p.find('  ') != -1:
                p = p.replace('  ', ' ')
            p_list.append(p)
            start_p += end_p+4
        answer.append((title,p_list))
        idx = end

    for title, p_list in answer:
        print('title : %s'%title)
        for p in p_list:
            print(p)
solv()