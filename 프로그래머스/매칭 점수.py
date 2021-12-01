def solution(word, pages):
    word = word.lower()
    web_info = make_web_info(word, pages)
    score, answer = calc_link_score(web_info)
    return answer


def calc_link_score(web_info):

    for url in web_info:
        now = web_info[url]
        for link in now['links']:
            if link not in web_info:
                continue
            web_info[link]['score'] += now['count'] / len(now['links'])

    link_score = 0
    answer = 0
    for url in web_info:
        score = web_info[url]['score']
        index = web_info[url]['index']
        if link_score < score:
            link_score = score
            answer = index
        elif link_score == score:
            answer = min(answer, index)
    return link_score, answer


def make_web_info(word, pages):
    web_info = {}
    index = 0

    for page in pages:
        url = search_url(page).strip()
        count = search_word(word,page)
        links = search_links(page, url)
        web_info[url] = {
            'index': index,
            'count': count,
            'links': links,
            'score': count
        }
        index += 1
    return web_info


def search_url(page):
    start = page.index('<meta property="og:url" content="') + len('<meta property="og:url" content="')
    end = start + page[start:].index('"/>')
    return page[start:end]


def search_word(word, page):
    count = 0
    page = page.lower()
    while True:
        index = page.find(word)
        if index == -1:
            return count
        if 0 < index:
            if not page[index - 1].isalpha() and not page[index+len(word)].isalpha():
                count += 1
        elif index == 0:
            if not page[index + len(word)].isalpha():
                count += 1
        page = page[index + len(word)-1:]


def search_links(page, url):
    body = page[page.index('<body>'):].lower()
    links = []
    try:
        while True:
            start = body.index('<a href="') + len('<a href="')
            end = start + body[start:].index('">')
            link = body[start:end].strip()
            if link != url:
                links.append(link)
            body = body[end + 3:]
    except:
        pass

    return links