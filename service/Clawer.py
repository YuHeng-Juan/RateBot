import os

from bs4 import BeautifulSoup
from urllib import request
import requests
from lxml import etree

def ticketInfo():
    inFo = ""
    resp = requests.get('https://www.ptt.cc/bbs/Japan_Travel/index.html')
    soup = BeautifulSoup(resp.text, 'html.parser')
    main_titles = soup.find_all('div', 'title')

    for title in main_titles:

        if "資訊" in title.text:
            inFo += title.text.strip() + "\n"
            inFo += "https://www.ptt.cc" + title.find("a")['href'] + "\n"

    return inFo

def imageInfo(url):
    print('IG url:' + url)
    imageUrl = ""
    resp = requests.get(url)
    soup = BeautifulSoup(resp.text, 'html.parser')
    image = soup.find("meta", property="og:image")

    imageUrl = image["content"]
    print('image url:' + imageUrl)

    return imageUrl

def exchangeRate(country):
    
    resp = requests.get("https://rate.bot.com.tw/xrt?Lang=zh-TW")
    byte_data = resp.content
    source_code = etree.HTML(byte_data)
    # print(source_code)
    bank_cash_buy = source_code.xpath('//*[@id="ie11andabove"]/div/table/tbody/tr[1]/td[2]')
    bank_cash_sell = source_code.xpath('//*[@id="ie11andabove"]/div/table/tbody/tr[1]/td[3]')
    bank_online_buy = source_code.xpath('//*[@id="ie11andabove"]/div/table/tbody/tr[1]/td[4]')
    bank_online_sell = source_code.xpath('//*[@id="ie11andabove"]/div/table/tbody/tr[1]/td[5]')
    result = "現金買入: " + bank_cash_buy[0].text.strip() + '\n' + "現金賣出: " + bank_cash_sell[0].text.strip() + '\n\n' + "即期買入: " + bank_online_buy[0].text.strip() + '\n' + "即期賣出: " + bank_online_sell[0].text.strip()
    return result
    # resp.encoding = "utf-8"
    # rateString = ""
    # soup = BeautifulSoup(resp.text, 'html.parser')
    # first_table = soup.find_all("table", class_="c-table is-pcRight")
    # # print(first_table[0])
    # for table in first_table:
    #     tbody = table.find("tbody")
    #     print(tbody.contents)
    # # print(first_table.string)
    # input()
    # index = 0
    # index2 =0
    # for table in first_table:
    #     index += 1
    #     if index == 5:
    #         main_tab = table.find_all('table')
    #         for table2 in main_tab:
    #             index2 += 1
    #             if index2 ==2:
    #                 index3 = 0
    #                 main_tr = table2.find_all('tr')
    #                 for tr in main_tr:
    #                     index3 += 1
    #                     if index3 == 3:
    #                         temp = ""
    #                         tdNum = 0
    #                         main_td = tr.find_all("td")
    #                         for td in main_td:
    #                             tdNum += 1
    #                             if tdNum != 7:
    #                                 if tdNum == 5:
    #                                     temp = temp + "即期:" + td.find("span").text +"\n"
    #                                 elif tdNum == 6:   
    #                                     temp = temp + "現鈔:" + td.find("span").text +"\n"
    #                                 else:
    #                                     temp = temp + td.find("span").text + "\n"
    #                         rateString += temp
    #                     if index3 == 4:
    #                         temp = ""
    #                         tdNum = 0
    #                         main_td = tr.find_all("td")
    #                         for td in main_td:
    #                             tdNum += 1
    #                             if tdNum > 3:
    #                                 if tdNum == 5:
    #                                     temp = temp + "即期:" + td.find("span").text +"\n"
    #                                 elif tdNum == 6:   
    #                                     temp = temp + "現鈔:" + td.find("span").text +"\n"
    #                                 else:
    #                                     temp = temp + td.find("span").text + "\n"
    #                         temp = temp + "\n"
    #                         rateString += temp
    # return rateString

    # index = 0
    # main_tr = first_table.find_all('tr')
    # for title in main_tr:
    #     index = index + 1
    #     if index == 2:
    #         temp = ""
    #         tdNum = 0
    #         main_td = title.find_all("td")
    #         for td in main_td:
    #             tdNum = tdNum + 1
    #             if tdNum != 4:
    #                 temp = temp + td.text + "|"

    #         temp = temp + "\n"
    #         rateString += temp

    #     if index == 3:
    #         temp = ""
    #         tdNum = 0
    #         main_td = title.find_all("td")
    #         for td in main_td:
    #             tdNum = tdNum + 1
    #             if tdNum != 4:
    #                 temp = temp + td.text + "|"

    #         temp = temp + "\n"
    #         rateString += temp

    # rateString += "\n連結:http://www.findrate.tw/"+country+"/"
    # return rateString

# def fruitPrice(fruit):
#     fruitString = ""
#     resp = requests.get("https://www.twfood.cc/fruit/"+fruit+")")
#     resp.encoding = "utf-8"
#     soup = BeautifulSoup(resp.text, 'html.parser')
#     table = soup.find_all('table', 'table-hover')
#     main_tr = table[0].find_all('tr')

#     index = 0
#     temp = ""
#     for tr in main_tr:
#         if index%3 == 0:
#             main_td = tr.find_all("th")
#             if temp != "":
#                 temp +="\n"

#             temp +=  main_td[0].text.strip()

#         if index%3 == 1:
#             main_str = tr.find_all("span")
#             price = tr.find_all("th","vege_chart_th_unit")
#             temp +="\n " + str(main_str[0].text).strip() +" "+ str(price[0].text).strip()

#         if index%3 == 2:
#             main_str = tr.find_all("span")
#             price = tr.find_all("th","vege_chart_th_unit")
#             temp +="\n " + str(main_str[0].text).strip() +" "+ str(price[0].text).strip()

#         index = index + 1

#     return temp



# def getSebUrl(url):
#     # 瀏覽器請求頭（大部分網站沒有這個請求頭可能會報錯）
#     print(url)
#     mheaders = {
#         'User-Agent': "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/22.0.1207.1 Safari/537.1"}
#     req = request.Request(url,headers=mheaders) #新增headers避免伺服器拒絕非瀏覽器訪問
#     page = request.urlopen(req)
#     html = page.read()
#     soup = BeautifulSoup(html.decode('utf-8'), 'html.parser')
#     body = soup.find(id="pins")
#     link = body.find_all("li")
#     next_link = []
#     for li_element in link:
#         # print(li_element.find('a').get('href'))
#         next_link.append(li_element.find('a').get('href'))

#     num = random.randint(1, len(next_link)-1)

#     return next_link[num]  # python3 python2版本直接返回html

# def getHtmlImgUrl(url):
#     print(url)
#     index = []
#     mheaders = {
#         'User-Agent': "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/22.0.1207.1 Safari/537.1"}
#     req = request.Request(url, headers=mheaders)  # 新增headers避免伺服器拒絕非瀏覽器訪問
#     page = request.urlopen(req)
#     html = page.read()
#     soup = BeautifulSoup(html.decode('utf-8'), 'html.parser')
#     body = soup.find(class_="pagenavi")
#     page = body.find_all("a")

#     for page_element in page:
#         # print(page_element.get('href').split('/'))
#         element = page_element.get('href').split('/')
#         if element[len(element)-1] != "":
#             index.append(int(element[len(element)-1]))

#     return url+"/"+str(random.randint(1, index[4]))

# def getImage(url):
#     print(url)
#     mheaders = {
#         'User-Agent': "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/22.0.1207.1 Safari/537.1"}
#     req = request.Request(url, headers=mheaders)  # 新增headers避免伺服器拒絕非瀏覽器訪問
#     page = request.urlopen(req)
#     html = page.read()
#     soup = BeautifulSoup(html.decode('utf-8'), 'html.parser')
#     body = soup.find(class_='main-image')
#     img = body.find('img').get('src')

#     return  img

# def getCk101Url(url):
#     print("getCk101Url url:" + url)
#     # 瀏覽器請求頭（大部分網站沒有這個請求頭可能會報錯）
#     index = []
#     mheaders = {
#         'User-Agent': "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/22.0.1207.1 Safari/537.1"}
#     req = request.Request(url,headers=mheaders) #新增headers避免伺服器拒絕非瀏覽器訪問
#     page = request.urlopen(req)
#     html = page.read()
#     soup = BeautifulSoup(html.decode('utf-8'), 'html.parser')
#     main = soup.find('div','bt-main-cont')
#     search_li = main.find_all('li')
#     for li in search_li:
#         element = li.find('a').get('href')
#         if not element is None:
#             index.append(element)

#     getOne = index[random.randint(0, len(index)-1)]
#     print("getCk101Url back url :" + getOne)
#     return getOne

# def getCk101Photo(url):
#     print("photo url:"+url)
#     index = []
#     mheaders = {
#         'User-Agent': "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/22.0.1207.1 Safari/537.1"}
#     req = request.Request(url, headers=mheaders)  # 新增headers避免伺服器拒絕非瀏覽器訪問
#     page = request.urlopen(req)
#     html = page.read()
#     soup = BeautifulSoup(html.decode('utf-8'), 'html.parser')
#     main_table = soup.find(id = 'lightboxwrap')
#     img_all = main_table.find_all('img')

#     for img in img_all:
#         element = img.get('file')
#         if not element is None:
#             index.append(element)

#     getOne = index[random.randint(0, len(index)-1)]
#     print("photo back url :" + getOne)
#     return getOne

# def SqlFindDataUrl():
#     #connect info
#     host = os.environ['DATABASE_HOST']
#     port = os.environ['DATABASE_PORT']
#     database = os.environ['DATABASE']
#     user = os.environ['DATABASE_USER']
#     passwd = os.environ['DATABASE_PASSWORD']

#     #construct connect string
#     conn = psycopg2.connect(database=database,host=host,user=user,password=passwd,port=port)
#     cur = conn.cursor()

#     #查共有幾個
#     sql = "SELECT count(*) FROM image"
#     cur.execute(sql)
#     rows=cur.fetchall()

#     #random其中一個
#     ranId = random.randint(1,int(rows[0][0]))
#     takeUrl = "SELECT title,url FROM image WHERE id ={0}".format(ranId)
#     cur.execute(takeUrl)
#     titleRow = cur.fetchall()

#     conn.commit() # 查询时无需，此方法提交当前事务。如果不调用这个方法，无论做了什么修改，自从上次调用#commit()是不可见的
#     cur.close()
#     conn.close()

#     return titleRow[0][1]

# def randomIgImage():
#     url = SqlFindDataUrl()
#     resp = requests.get(url)
#     soup = BeautifulSoup(resp.text, 'html.parser')
#     main_table = soup.find('article')
#     img_all = main_table.find_all('img')




if __name__ == '__main__':
    # Test Function
    # IgUrl = "https://www.instagram.com/p/BymVt2NH5OE/?igshid=7jpeb1f596h6"
    IString = exchangeRate("USD")
    # IArray = getCk101Photo('https://ck101.com/thread-5017396-1-1.html')
    # IArray = getImage('https://www.mzitu.com/187752/16')
    # SData = randomIgImage()

    print(IString)
