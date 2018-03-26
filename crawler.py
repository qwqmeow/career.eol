#!/usr/bin/env python
#-*-coding:utf-8-*-

import controler
import downloader
import pageparser
import time
import sqlite3
import string
import os
import sys
reload(sys)
sys.setdefaultencoding('utf-8')






def main(entrance):
    
    print "entrance:{}".format(entrance)

    entrance_html = downloader.get_html(entrance)
    classify_url_list = pageparser.get_classify(entrance_html)

    for classify_url in classify_url_list:
        
        print 'classify_url:{}'.format(classify_url)
        classify_html = downloader.get_html(classify_url)
        careers_url_list = pageparser.get_careers(classify_html)

        for career in careers_url_list:
            print 'career:{}'.format(career)
            career_html = downloader.get_html(career)
            pagetitle,class_,who_can_do = pageparser.get_info(career_html)    



            controler.write_data(pagetitle,class_, who_can_do)
            # print 'pagetitle:{},who_can_do:{}'.format(pagetitle, who_can_do)



if __name__ == '__main__':
    main('http://career.eol.cn/html/sy/zhiye/')
