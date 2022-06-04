from urllib.parse import urljoin
from bs4 import BeautifulSoup
import requests

def get_soup(url):
    return BeautifulSoup(requests.get(url).text, 'html.parser')

# search = input("Masukkan kata kunci: ")
# url = "https://www.google.com/search?q=" + search
# soup = get_soup(url)
# for i in soup.find_all('a'):
#     print(i.get('href'))

def getGoPackage(msg, num):
    url = "https://pkg.go.dev/search?q=" + msg
    soup = get_soup(url)
    #Get value tag a with beautifoulsoup in article tag
    tag = soup.find_all('article')
    
    #Get value tag a with beautifulsoup in article tag
    tag_a = tag[0].find_all('a')
    
    total=1
    for i in tag_a:
        
        #Get value tag a with beautifulsoup in article tag
        # tag_a_href = tag_a[i].get('href')
        #Get value tag a with beautifulsoup in article tag
        tag_a_text = i.get_text()
        print("{}. akan mengambil: {}".format(total, tag_a_text))
        total+=1
        if total == num+1:
            break
    
    return True

def getGoBlog(msg):
    url = "https://pkg.go.dev/search?q=" + msg
    soup = get_soup(url)

    #Get value with beautifoulsoup in class SearchSnippet
    SearchSnippet = soup.find_all('div', class_='SearchSnippet')

    #Get href with beautifulsoup in class SearchSnippet
    judul = SearchSnippet[0].find_all('a')
    url_hasil_search = "https://pkg.go.dev/" + judul[0].get('href')
    soup = get_soup(url_hasil_search)

    #Get value with beautifoulsoup in class Documentation-indexList
    Documentation_indexList = soup.find_all('ul', class_='Documentation-indexList')

    #Get value li with beautifoulsoup
    Documentation_indexList_li = Documentation_indexList[0].find_all('a')

    # Get all text with beautifulsoup
    for i in Documentation_indexList_li:
        text = i.get_text().split(' ')
        if (text[0] == 'type'):
            print(i.get_text())
        elif (text[0] == 'func'):
            print('\t' + i.get_text())
    return True

def main():   
    # getGoPackage("llrb", 10)
    getGoBlog("llrb+petar")

if __name__ == '__main__':
    main()
