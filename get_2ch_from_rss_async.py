from lxml import etree
import sqlite3
import requests
import re
import os
import time
import json
import pprint
import gevent
from gevent import monkey,pool
monkey.patch_socket()


def remove_parentheses(text):
    return re.sub(r'\{.+?\}','',text)

def read_rss_feed(url):
    global count

    # news_field = [field.attname for field in News._meta.fields]
    try:
        root = etree.fromstring(requests.get(url).content)
    except:
        return

    # conn = sqlite3.connect('db.sqlite3')
    # pp = pprint.PrettyPrinter(indent=4)
    if 'atom' in url:
        title = root[0].text

        items = root.xpath("//*[local-name()='entry']")
        for item in items:
            entry = {'base_site':title}
            for content in item:
                label = remove_parentheses(content.tag)
                if label == 'title' or label == 'subject':
                    entry[label] = content.text
                if label == 'link':
                    entry['link'] = content.get('href')
                if label == 'issued':
                    entry['date'] = content.text
            # print('----------------------------------------------------------------------')
            # pp.pprint(entry)
            # print('----------------------------------------------------------------------')
            if not entry['link'] in all_links:
                News(**entry).save()

    else:
        title = root[0][0].text
        items = root.xpath("//*[local-name()='item']")
        for item in items:
            entry = {'base_site':title}
            for content in item:
                label = remove_parentheses(content.tag)
                if label == 'title' or label == 'link' or label == 'date' or label == 'subject':
                    entry[label] = content.text
            # print('----------------------------------------------------------------------')
            # pp.pprint(entry)
            # print('----------------------------------------------------------------------')
            if not entry['link'] in all_links:
                News(**entry).save()

def main():
    # rss_feeder = [('vipper','http://vippers.jp/index.rdf'),]
    p = pool.Pool(20)

    all_news = News.objects.all()
    global all_links
    all_links = []
    for news in all_news:
        all_links.append(news.link)

    with open('rss_list.txt') as f:
        rss_feeder = f.read().split('\n')

    threads = []
    for url in rss_feeder:
        threads.append(p.spawn(read_rss_feed, url))
    gevent.joinall(threads,timeout=5, raise_error=True)

if __name__ == '__main__':
    os.environ['DJANGO_SETTINGS_MODULE'] = 'mysite.settings'
    from news.models import News
    main()

