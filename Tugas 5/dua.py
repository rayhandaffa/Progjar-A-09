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
    url = "https://www.google.com/search?q=" + msg
    soup = get_soup("https://go.dev/doc/")
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

def main():   
    getGoPackage("llrb", 10)

if __name__ == '__main__':
    main()
