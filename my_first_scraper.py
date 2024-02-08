from bs4 import BeautifulSoup
import requests

giturl = "https://github.com/trending"

def request_github_trending(url):
    res = requests.get(url)
    res_code = res.status_code
    if res_code!= 200:
        print("ERROR")
        return
    return res

req = request_github_trending(giturl)


def extract(page):
    getAll = BeautifulSoup(page.text, "html.parser")
    articleList = getAll.find_all('article', class_='Box-row')
    return articleList


repo = extract(req)
# print(repo)

def transform(html_repos):
    data = []
    for i in html_repos[:25]:
        line = {'developer': '', 'repository_name': '', 'nbr_stars': ''}
        line['developer'] = i.h1.a.span.text.strip().split(" ")[0]
        line['repository_name'] = i.h1.a.text.strip().split(" ")[7]
        line['nbr_stars'] = i.find('a', class_='Link--muted d-inline-block mr-3').text.strip()
        
        # print(i.h1.a.span.text.strip())
        # print(i.h1.a.text.strip().split(" "))
        # print(i.find('a', class_='Link--muted d-inline-block mr-3').text.strip())

        data.append(line)
    return data       


data = transform(repo[1])
print(data)
def format(repositories_data):
    csv = ""
    arr = []
    for i in repositories_data:
        list = i.values()
        arr.append(",".join(list))
    csv="\n".join(arr)
    return csv

print(format(data))
# page = request_github_trending(giturl)
# repo_list = extract(page)
# print(transform(repo_list))
# print(format([{'developer': 'NAME', 'repository_name': 'REPOS_NAME', 'nbr_stars': 'NBR_STARS'},{'developer': 'NAME1', 'repository_name': 'REPOS_NAME_1', 'nbr_stars': 'NBR_STARS_1'}]))