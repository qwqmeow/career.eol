#!/usr/bin/env python
#-*-coding:utf-8-*-

from bs4 import BeautifulSoup
import downloader
import time
from lxml import etree
import sys
reload(sys)
sys.setdefaultencoding('utf-8')


def get_classify(html):
    main_url = 'http://career.eol.cn/html/sy/zhiye/'
    classify_url_list = []
    soup = BeautifulSoup(html, "html.parser")
    classify = soup.select('a[class="blue01_12"]')
    for x in classify:
        classify_url_list.append(main_url + x.get('href'))

    print classify_url_list
    return classify_url_list


def get_careers(html):
    main_url = 'http://career.eol.cn/html/sy/zhiye/c/'
    
    careers_url_list = []

    soup = BeautifulSoup(html, "html.parser")

    for x in soup.select('td[class="line_23"]')[1].select('a[class="blue01_14"]'):
        if x.text == u'[详细]':
            careers_url_list.append(main_url + x.get('href'))

    return careers_url_list


def get_info(html):
    who_can_do=''
    
    soup = BeautifulSoup(html, "html.parser")
    text = soup.select('td[class="black_14a"]')[0].text

    pagetitle = soup.select('h1[id="pagetitle"]')[0].text
    precontent = soup.select('div[id="precontent"]')
    class_ = precontent[0].select('p')[0].text

    if not text.find(u'【谁能做】') == -1:
        start_index = text.find(u'【谁能做】')
        end_index = text.find(u'【小贴士】')
        
        who_can_do = text[start_index+5:end_index]
    
    if not text.find(u'从业要求') == -1:
        start_index = text.find(u'从业要求')
        end_index = text.find(u'优秀者特质')
        
        who_can_do = text[start_index+5:end_index]
    
    if not text.find(u'从业素质要求') == -1:
        start_index = text.find(u'从业素质要求')
        end_index = text.find(u'职位认证')
        if end_index == -1:
            end_index = text.find(u'职位背景')
        
        who_can_do = text[start_index+5:end_index]    
        


    return pagetitle,class_,who_can_do
        


