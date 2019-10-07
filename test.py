from urllib.request import urlopen
from bs4 import BeautifulSoup
import pandas as pd



khu_janghak_board = []


url = 'https://janghak.khu.ac.kr/board/bbs/board.php?bo_table=06_01&page=1&pmi-sso-return2=none'
html = urlopen(url)
html = BeautifulSoup(html, "html.parser")
khu_janghak = html.find("table", {"class": "board_list"}).findAll("tr")[1:]


khu_janghak_num = khu_janghak[-15].find("td", {"class": "num"})
khu_janghak_title = khu_janghak[-15].find("td", {"class": "subject"})
khu_janghak_user = khu_janghak[-15].find("td", {"class": "name"})
khu_janghak_date = khu_janghak[-15].find("td", {"class": "datetime"})
khu_janghak_count = khu_janghak[-15].find("td", {"class": "hit"})
khu_janghak_link = khu_janghak[-15].find("td", {"class": "subject"}).find("a")
khu_janghak_temp = [khu_janghak_num.get_text().strip(), khu_janghak_title.get_text().strip(),
                                khu_janghak_user.get_text().strip(), khu_janghak_date.get_text().strip(),
                                khu_janghak_count.get_text().strip(),
                                'https://janghak.khu.ac.kr/board' + khu_janghak_link.attrs['href'].strip()[2:]]

khu_janghak_board.append(khu_janghak_temp)

khu_main_board = pd.DataFrame(khu_janghak_board, columns=['번호', '제목', '글쓴이', '날짜', '조회수', '링크'])
khu_main_board.to_csv('khu_janghak.csv')








