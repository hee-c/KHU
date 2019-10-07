from urllib.request import urlopen
from bs4 import BeautifulSoup
import pandas as pd
import re

temp_1 = 'http://kbiz.khu.ac.kr/board5/bbs/board.php?bo_table=05_04_01&sca=%EA%B5%AD%EC%A0%9C%EA%B5%90%EB%A5%98'
temp_2 = urlopen(temp_1)
temp_2 = BeautifulSoup(temp_2, "html.parser")
max_pages = temp_2.find("div", {"id": "bo_list_total"}).span.get_text()
max_pages = re.findall("\d+", max_pages)

if len(max_pages) > 1:
    max_pages = max_pages[0]+max_pages[1]
else:
    max_pages = max_pages[0]

max_pages = int(max_pages)

'''
khu_management_board.to_csv('khu_management_Undergraduate.csv')
http://kbiz.khu.ac.kr/board5/bbs/board.php?bo_table=05_04_01&sca=%ED%95%99%EC%82%AC%EC%95%88%EB%82%B4
khu_management_board.to_csv('khu_management_Scholarship.csv')
http://kbiz.khu.ac.kr/board5/bbs/board.php?bo_table=05_04_01&sca=%EC%9E%A5%ED%95%99%EC%95%88%EB%82%B4
khu_management_board.to_csv('khu_management_International.csv')
http://kbiz.khu.ac.kr/board5/bbs/board.php?bo_table=05_04_01&sca=%EA%B5%AD%EC%A0%9C%EA%B5%90%EB%A5%98
khu_management_board.to_csv('khu_management_Intern.csv')
http://kbiz.khu.ac.kr/board5/bbs/board.php?bo_table=05_04_01&sca=%ED%98%84%EC%9E%A5%EC%8B%A4%EC%8A%B5
khu_management_board.to_csv('khu_management_Job.csv')
http://kbiz.khu.ac.kr/board5/bbs/board.php?bo_table=05_04_01&sca=%EC%B7%A8%EC%97%85
khu_management_board.to_csv('khu_management_Startup.csv')
http://kbiz.khu.ac.kr/board5/bbs/board.php?bo_table=05_04_01&sca=%EC%B0%BD%EC%97%85
khu_management_board.to_csv('khu_management_CPA.csv')
http://kbiz.khu.ac.kr/board5/bbs/board.php?bo_table=05_04_01&sca=%EC%B2%AD%ED%98%84%EC%9E%AC
'''