from urllib.request import urlopen
from bs4 import BeautifulSoup
import pandas as pd
import re

def khu_management(category, category_name):

    khu_management_board = []

    temp_1 = 'http://kbiz.khu.ac.kr/board5/bbs/board.php?bo_table=05_04_01&sca={}'.format(category)
    temp_2 = urlopen(temp_1)
    temp_2 = BeautifulSoup(temp_2, "html.parser")
    max_pages = temp_2.find("div", {"id": "bo_list_total"}).span.get_text()
    max_pages = re.findall("\d+", max_pages)

    if len(max_pages) > 1:
        max_pages = max_pages[0] + max_pages[1]
    else:
        max_pages = max_pages[0]

    max_pages = int(max_pages) // 15 + 1

    for page in range(1, max_pages+1):
        url = 'http://kbiz.khu.ac.kr/board5/bbs/board.php?bo_table=05_04_01&sca={}&page={}'.format(category, page)
        html = urlopen(url)
        html = BeautifulSoup(html, "html.parser")
        khu_management = html.find("div", {"class": "tbl_head01 tbl_wrap"}).tbody.findAll("tr")

        for board in range(0, len(khu_management)):
            khu_management_temp = []
            khu_management_num = khu_management[board].find("td", {"class": "td_num"})
            khu_management_title = khu_management[board].find("td", {"class": "td_subject"}).findAll("a")[1]
            khu_management_user = khu_management[board].find("td", {"class": "td_name sv_use"})
            khu_management_date = khu_management[board].find("td", {"class": "td_date"})
            khu_management_count = khu_management[board].findAll("td", {"class": "td_num"})[1]
            khu_management_link = khu_management[board].find("td", {"class": "td_subject"}).findAll("a")[1]
            khu_management_temp = [khu_management_num.get_text().strip(), khu_management_title.get_text().strip(),
                                   khu_management_user.get_text().strip(), khu_management_date.get_text().strip(),
                                   khu_management_count.get_text().strip(), khu_management_link.attrs['href'].strip()]
            khu_management_board.append(khu_management_temp)

        print(page)

    khu_management_board = pd.DataFrame(khu_management_board, columns=['번호', '제목', '글쓴이', '날짜', '조회수', '링크'])
    khu_management_board.to_csv('KHU_Management_{}.csv'.format(category_name))


khu_management('%ED%95%99%EC%82%AC%EC%95%88%EB%82%B4', 'Undergraduate')
khu_management('%EC%9E%A5%ED%95%99%EC%95%88%EB%82%B4', 'Scholarship')
khu_management('%EA%B5%AD%EC%A0%9C%EA%B5%90%EB%A5%98', 'International')
khu_management('%ED%98%84%EC%9E%A5%EC%8B%A4%EC%8A%B5', 'Intern')
khu_management('%EC%B7%A8%EC%97%85', 'Job')
khu_management('%EC%B0%BD%EC%97%85', 'Startup')
khu_management('%EC%B2%AD%ED%98%84%EC%9E%AC', 'CPA')
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