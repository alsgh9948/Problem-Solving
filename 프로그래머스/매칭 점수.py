def solution(word, pages):
    page_info = {}

    for page in pages:
        link = get_link(page)
        page_info[link] = {
            'basic_score': count_keyword(page, word.lower()),
            'links': check_link(page),
        }

    score_order = []
    for target in page_info.keys():
        link_score = 0
        for link in page_info.keys():
            if target in page_info[link]['links']:
                link_score += page_info[link]['basic_score'] / len(page_info[link]['links'])
        score_order.append((len(score_order), page_info[target]['basic_score'] + link_score))
    answer = 0
    score_order.sort(key=lambda x: (-x[1], x[0]))
    return score_order[0][0]


def get_link(page):
    start = page.find('<head>')
    while True:
        meta_start = page.find('<meta', start)
        meta_end = page.find('>',meta_start)
        meta = page[meta_start:meta_end]
        if meta.find('property="og:url"') >= 0:
            url_start = meta.index('content="') + len('content="')
            url_end = meta.index('"', url_start)
            return meta[url_start:url_end]
        start = meta_end+1

def count_keyword(page, keyword):
    word = ''
    count = 0
    for c in page:
        if c.isalpha():
            word += c
        else:
            if word.lower() == keyword:
                count += 1
            word = ''
    return count


def check_link(page):
    links = []
    start = 0
    while True:
        a_start = page.find('<a href="', start)
        if a_start == -1:
            break
        a_end = page.find('</a>',a_start)

        link_start = a_start + len('a_start')
        link_end = page.find('">', link_start)
        links.append(page[link_start:link_end])
        start = a_end+4
    return links

a = "Muzi"
b = ["<html lang=\"ko\" xml:lang=\"ko\" xmlns=\"http://www.w3.org/1999/xhtml\">\n<head>\n  <meta charset=\"utf-8\">\n  <meta property=\"og:url\" content=\"https://careers.kakao.com/interview/list\"/>\n</head>  \n<body>\nMuzi<a href=\"https://careers.kakao.com/interview/list\"></a>#!MuziMuzi!)jayg07con&&\n\n</body>\n</html>", "<html lang=\"ko\" xml:lang=\"ko\" xmlns=\"http://www.w3.org/1999/xhtml\">\n<head>\n  <meta charset=\"utf-8\">\n  <meta property=\"og:url\" content=\"https://www.kakaocorp.com\"/>\n</head>  \n<body>\ncon%\tmuzI92apeach&2<a href=\"https://hashcode.co.kr/tos\"></a>\n\n\t^\nMuziMuzi Muzi</body>\n</html>"]
print(solution(a,b))