import sys
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup
import json


driver = webdriver.Chrome()


#driver = webdriver.Chrome()
driver.get('https://mops.twse.com.tw/mops/web/t100sb07_1')

#輸入股票代碼
#
# stockid="2330"
stockid = ["6560 ", "6561 "]

newData=[]

for var,index in enumerate(stockid):


    driver.find_element_by_id('co_id').send_keys(index)#找id=email
    driver.find_element_by_id('co_id').send_keys(Keys.ENTER)
    time.sleep(1) #這很重要

    soup = BeautifulSoup(driver.page_source, 'html.parser')
    table=soup.find('table', class_ = 'hasBorder')

    table_all=table.find_all('td')


    table_data=[]

    for i in range(0,len(table_all)):
        table_data.append(table_all[i].text)


    tablec_dict = {
                #召開法人說明會日期：
                "date": table_data[1].replace('\n',''),
                #召開法人說明會地點：
                "location": table_data[3].replace('\n',''),

                #法人說明會擇要訊息：：
                "import_info": table_data[5].replace('\n',''),
                #法人說明會簡報內容中文：：
                "chinese_file": table_data[8].replace('\n',''),
                #法人說明會簡報中文內容連結：：
                "chinese_href":'https://mops.twse.com.tw/nas/STR/'+table_data[8].replace('\n',''),
                #法人說明會簡報內容英文：：
                "english_file": table_data[10].replace('\n',''),

                #法人說明會簡報英文內容連結：：
                "english_href":'https://mops.twse.com.tw/nas/STR/'+table_data[10].replace('\n',''),

                #法人說明會相關資訊：
                "info": table_data[13].replace('\n',''),

                #影音連結：
                "video": table_data[14].replace('\n','').replace('\xa0',''),

                #其他應敘明事項：
                "other": table_data[16],

                }

    newData += [tablec_dict]
    driver.find_element_by_id('co_id').clear()


driver.quit()
#driver.close()

# newData= json.dumps(newData)
# print(newData)





#https://mops.twse.com.tw/mops/nas/STR/

