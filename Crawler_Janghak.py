from urllib.request import urlopen
from bs4 import BeautifulSoup
import pandas as pd

def khu_janghak(max_pages):

    khu_janghak_board = []

    for page in range(1, max_pages + 1):
        url = 'https://janghak.khu.ac.kr/board/bbs/board.php?bo_table=06_01&page={}&pmi-sso-return2=none'.format(page)
        html = urlopen(url)
        html = BeautifulSoup(html, "html.parser")
        khu_janghak = html.find("table", {"class": "board_list"}).findAll("tr")[1:]

        for board in range(-15, 0):
            khu_janghak_num = khu_janghak[board].find("td", {"class": "num"})
            khu_janghak_title = khu_janghak[board].find("td", {"class": "subject"})
            khu_janghak_user = khu_janghak[board].find("td", {"class": "name"})
            khu_janghak_date = khu_janghak[board].find("td", {"class": "datetime"})
            khu_janghak_count = khu_janghak[board].find("td", {"class": "hit"})
            khu_janghak_link = khu_janghak[board].find("td", {"class": "subject"}).find("a")
            khu_janghak_temp = [khu_janghak_num.get_text().strip(), khu_janghak_title.get_text().strip(),
                                khu_janghak_user.get_text().strip(), khu_janghak_date.get_text().strip(),
                                khu_janghak_count.get_text().strip(),
                                'https://janghak.khu.ac.kr/board' + khu_janghak_link.attrs['href'].strip()[2:]]

            khu_janghak_board.append(khu_janghak_temp)
        print(page)

    khu_main_board = pd.DataFrame(khu_janghak_board, columns=['번호', '제목', '글쓴이', '날짜', '조회수', '링크'])
    khu_main_board.to_csv('khu_Janghak.csv')


khu_janghak(101)





