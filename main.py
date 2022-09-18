import requests
from fake_useragent import UserAgent
from bs4 import BeautifulSoup


url = ''
ua = UserAgent()
headers = {'user-agent': f'{ua.random}'}


def get_pc():
    r = requests.get(url=url, headers=headers)
    with open('olxa.html', 'w', encoding='utf-8') as f:
        f.write(r.text)

    with open('olxa.html', encoding='utf-8') as f:
        src = f.read()
    soup = BeautifulSoup(src, 'lxml')
    info = soup.find_all('div', class_='a-card__content')
    #page = soup.find('div', class_='pagination').text
    #print(page)
    for item in info:
        href = item.find('a').get('href')
        r = requests.get(url=href, headers=headers)
        #with open('market.html','w', encoding='utf-8') as g:
            #g.write(r.text)
        with open('market.html', encoding='utf-8') as g:
            src = g.read()

        all_comps = []
        soup = BeautifulSoup(src, 'lxml')
        title = soup.find('div', class_='show-header').text.strip()
        description = soup.find('div', class_='description').text
        price = soup.find('dl', class_='value').text.strip()
        date = soup.find('div', class_='text').text.strip()
        #print(f'{title}\n{description}\t{price}\t{div}')
        all_comps.append({
            'title': title,
            'description': description,
            'price': price,
            'date': date
            })
        print(all_comps)

def main():
    get_pc()

if __name__ == '__main__':
    main()