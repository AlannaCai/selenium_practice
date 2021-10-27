from selenium.webdriver import Chrome
import time
from selenium.webdriver.support.ui import Select
from bs4 import BeautifulSoup
import pandas as pd 
import matplotlib.pyplot as plt

driver = Chrome("chromedriver.exe")
driver.get("https://www.twse.com.tw/zh/page/trading/fund/T86.html")

time.sleep(2)

# sp1 = BeautifulSoup(driver.page_source,'html.parser')
# date = (sp1.find_all("select"))
# year = date[0].find_all('option')
# month = date[1].find_all('option')
# day = date[2].find_all('option')

# daylist = []
# for i in range(len(day)):
#     if ('(日)' not in day[i].text) and ('(六)' not in day[i].text):        
#         # daylist.append(day[i].text)
#         day1 = day[i].text
driver.find_element_by_name("yy").send_keys("民國 110 年") #年
driver.find_element_by_name("mm").send_keys("10月")  #月
driver.find_element_by_name("dd").send_keys("06")  #日
driver.find_element_by_name("selectType").send_keys(
            "全部(不含權證、牛熊證、可展延牛熊證")
driver.find_element_by_xpath(
            '//*[@id="main-form"]/div/div/form/a').click() # 查詢
        
time.sleep(3)
driver.find_element_by_name("report-table_length").send_keys("全部")

time.sleep(3)        

sp1 = BeautifulSoup(driver.page_source,'html.parser')
table = (sp1.find_all("table"))
# type(table[0])
df = pd.read_html(str(table[0]))[0]
#print(df)

df['投信買進張數'] = df.投信買進股數 / 1000
df = df.sort_values(['投信買進張數'],ascending=False)
df_no0 = df.iloc[0:30]

plt.rcParams['axes.linewidth'] = 0.1
plt.bar(df_no0.證券名稱, df_no0.投信買進張數, width=0.8, 
         color = 'red', linewidth = 2)
plt.xticks(rotation=45, ha='right',fontsize=15)
plt.show()

driver.close()

