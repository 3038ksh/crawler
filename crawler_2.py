import requests
from bs4 import BeautifulSoup

class Crawler(object):
    @staticmethod
    def crawl(url):
        # 코드 긁어오기
        source_code = requests.get(url)
        # 텍스트로 바꾸기
        plain_text = source_code.text
        # 파싱
        soup = BeautifulSoup(plain_text, "lxml")
        # 원하는 데이터 리스트 만들기
        item_list = soup.find_all("div", attrs={"class": "items-wrapper"})
        # 만약 Dewey class no가 없을 경우 LC classification 저장용
        ret_str = ""

        for item in item_list:
            # 원하는 데이터 또 찾기
            item_h3 = item.find_all('h3')
            for h3 in item_h3:
                # Dewey 찾기
                if h3.text == "Dewey class no.":
                    print(item.find("span", attrs={"dir":"ltr"}).text)
                    return item.find("span", attrs={"dir": "ltr"}).text
                # LC classification 찾기
                if h3.text == "LC classification":
                    print(item.find("span", attrs={"dir": "ltr"}).text)
                    ret_str = item.find("span", attrs={"dir": "ltr"}).text
                # 검색은 되지만 Dewey, LC classification 없을 경우
                if h3.text == "ISBN":
                    ret_str = "No Dewey & LC classification"
                    print(ret_str)
        # 검색했을 때 아무것도 안 나온 경우
        if (ret_str == ""):
            ret_str = "NOTHINGGGGG"
            print(ret_str)

        return ret_str