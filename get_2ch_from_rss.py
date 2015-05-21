from lxml import etree
import sqlite3
import requests
import re
import os
import json
import pprint
import asyncio
import aiohttp

def remove_parentheses(text):
    return re.sub(r'\{.+?\}','',text)

def read_rss_feed(url):

    conn = sqlite3.connect('db.sqlite3')
    # news_field = [field.attname for field in News._meta.fields]

    try:
        root = etree.fromstring(requests.get(url,headers={'User-Agent': 'My API Robot'}).content)
    except:
        return

    pp = pprint.PrettyPrinter(indent=4)
    if 'atom' in url:
        title = root[0].text

        items = root.xpath("//*[local-name()='entry']")
        for item in items[:1]:
            entry = {'base_site':title}
            for content in item:
                label = remove_parentheses(content.tag)
                if label == 'title' or label == 'subject':
                    entry[label] = content.text
                if label == 'link':
                    entry['link'] = content.get('href')
                if label == 'issued':
                    entry['date'] = content.text
                if label == 'author':
                    entry['creator'] = content[0].text
            print('----------------------------------------------------------------------')
            pp.pprint(entry)
            print('----------------------------------------------------------------------')
            # News(**entry).save()

    else:
        title = root[0][0].text
        items = root.xpath("//*[local-name()='item']")
        for item in items[:1]:
            entry = {'base_site':title}
            for content in item:
                label = remove_parentheses(content.tag)
                if label == 'title' or label == 'link' or label == 'date' or label == 'subject' or label == 'creator':
                    entry[label] = content.text
            print('----------------------------------------------------------------------')
            pp.pprint(entry)
            print('----------------------------------------------------------------------')
            # News(**entry).save()



@asyncio.coroutine
def print_magnet(query):
    url = 'http://thepiratebay.se/search/{}/0/7/0'.format(query)
    page = yield from get(url, compress=True)
    magnet = first_magnet(page)
    print('{}: {}'.format(query, magnet))

@asyncio.coroutine
def get(*args, **kwargs):
    response = yield from aiohttp.request('GET', *args, **kwargs)
    return (yield from response.read_and_close(decode=True))

def first_magnet(page):
    soup = etree.fromstring(page)
    a = soup.find('a', title='Download this torrent using magnet')
    return a['href']

distros = ['archlinux', 'ubuntu', 'debian']
loop = asyncio.get_event_loop()
f = asyncio.wait([print_magnet(d) for d in distros])
loop.run_until_complete(f)

def main():
    # rss_feeder = [('vipper','http://vippers.jp/index.rdf'),]
    with open('rss_list.txt') as f:
        rss_feeder = f.read().split('\n')

    for url in rss_feeder:
        read_rss_feed(url)


if __name__ == '__main__':
    os.environ['DJANGO_SETTINGS_MODULE'] = 'mysite.settings'
    from news.models import News
    main()

