from urllib.request import urlopen
from bs4 import BeautifulSoup
import pandas as pd

def khu_main(max_pages, category):

    khu_main_board = []

    for page in range(1, max_pages+1):
        url = 'https://www.khu.ac.kr/kor/notice/list.do?page={}&category={}'.format(page, category)
        html = urlopen(url)
        html = BeautifulSoup(html, "html.parser")
        khu_main = html.find("table", {"class": "board01"}).tbody.findAll("tr")
        for board in range(0, len(khu_main)):
            khu_main_temp = []
            khu_main_num = khu_main[board].find("td", {"class": "col01"})
            khu_main_campus = khu_main[board].find("td", {"class": "col02"}).span
            khu_main_title = khu_main[board].find("p", {"class": "txt06"})
            khu_main_user = khu_main[board].find("td", {"class": "col03"})
            khu_main_date = khu_main[board].find("td", {"class": "col04"})
            khu_main_count = khu_main[board].find("td", {"class": "col05"})
            khu_main_link = khu_main[board].find("td", {"class": "col02"}).find("a")
            khu_main_temp = [khu_main_num.get_text().strip(), khu_main_campus.get_text().strip(),
                             khu_main_title.get_text().strip(),
                             khu_main_user.get_text().strip(), khu_main_date.get_text().strip(),
                             khu_main_count.get_text().strip(),
                             "https://www.khu.ac.kr/kor/notice/" + khu_main_link.attrs['href'].strip()]
            khu_main_board.append(khu_main_temp)

        print(page)

    khu_main_board = pd.DataFrame(khu_main_board, columns=['번호', '캠퍼스', '제목', '글쓴이', '날짜', '조회수', '링크'])
    khu_main_board.to_csv('khu_main_{}.csv'.format(category))


khu_main(115, 'UNDERGRADUATE')
khu_main(55, 'SCHOLARSHIP')
khu_main(12, 'SCHEDULE')
khu_main(80, 'CREDIT')
khu_main(37, 'EVENT')
khu_main(1006, 'GENERAL')

'''
일반(부분 크롤링)
9페이지
https://www.khu.ac.kr/kor/notice/list.do?page=9&category=GENERAL
학사(전체 크롤링)
91페이지
https://www.khu.ac.kr/kor/notice/list.do?category=UNDERGRADUATE&page=1
장학(부분 크롤링)
5페이지
https://www.khu.ac.kr/kor/notice/list.do?category=SCHOLARSHIP&page=1
시간표 변경(부분 크롤링)
9페이지
https://www.khu.ac.kr/kor/notice/list.do?category=SCHEDULE&page=1
교내학점교류(첫페이지 크롤링)
1페이지
https://www.khu.ac.kr/kor/notice/list.do?category=CREDIT&page=1
행사(첫페이지 크롤링)
1페이지
https://www.khu.ac.kr/kor/notice/list.do?category=EVENT&page=1
'''