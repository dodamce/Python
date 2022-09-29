import time

from selenium import webdriver
from selenium.webdriver.common.by import By
import re
from lxml import etree

driver = webdriver.Chrome()
su = input("请输入账号")
go = input("请输入密码")
while True:
    try:
        driver.get("http://zhzb.nuc.edu.cn/cas/login?service=http%3A%2F%2Fnewi.nuc.edu.cn%2Fpersonal-center")

        # 登录
        user = driver.find_element(By.XPATH, '//*[@id="username"]')
        user.send_keys(su)
        key = driver.find_element(By.XPATH, '//*[@id="ppassword"]')
        key.send_keys(go)
        submit = driver.find_element(By.XPATH, '//*[@id="dl"]')
        submit.click()
        break
    except:
        pass

# 进入业务直通车
while True:
    try:
        # print(driver.page_source)
        log = driver.find_element(By.XPATH, '//*[@id="header"]/div/div/ul/li[3]/a')
        log.click()

        # 页面跳转
        path = re.findall(
            '<a href="(.*?)" target="_blank" style="background-color: rgb.*?;"><img src="/img/piclib/system-icon05.png"><p>教务系统</p></a>',
            driver.page_source)
        driver.get(path[0])
        break
    except:
        # print('出错，请等待页面响应')
        pass

# 进入选课界面
while True:
    try:
        root = 'http://222.31.49.139/jwglxt'
        # print(driver.page_source)
        # <a tabindex="-1" onclick="clickMenu('N253512','/xsxk/zzxkyzb_cxZzxkYzbIndex.html','自主选课','null'); return false;" href="javascript:void(0);" rel="noopener noreferrer" target="_blank">自主选课</a>

        find = etree.HTML(driver.page_source)
        cheat = str(find.xpath('//*[@id="cdNav"]/ul/li[3]/ul/li[2]/a/@onclick')[0])
        # onclick="clickMenu('N253512','/xsxk/zzxkyzb_cxZzxkYzbIndex.html','自主选课','null'); return false;"
        cheat = cheat.split('\'')
        # print(cheat[1], cheat[3])
        driver.get(root + cheat[3] + f"?gnmkdm={cheat[1]}&layout=default&su={su}")
        break
    except:
        print('出错，请等待页面响应')
        pass

# print(driver.page_source)

# 选择信息与通信工程,并查询课程
select = driver.find_element(By.XPATH, '//*[@id="searchBox"]/div/div[3]/div[2]/div/div[1]/ul/li[5]/a')
select.click()
have = driver.find_element(By.XPATH, '//*[@id="searchBox"]/div/div[3]/div[13]/div/div/ul/li[1]/a')
have.click()
button = driver.find_element(By.XPATH, '//*[@id="searchBox"]/div/div[1]/div/div/div/div/span/button[1]')
button.click()

# 将所有的课程列出来
while True:
    try:
        more = driver.find_element(By.XPATH, '//*[@id="more"]/font/a')
        more.click()
    except:
        print(driver.page_source)
        break

# 选择具体课程，这里的逻辑以后在实现
show = driver.find_element(By.XPATH, '//*[@id="contentBox"]/div[2]/div[2]')
show.click()
my = driver.find_element(By.XPATH,
                         '/html/body/div[1]/div/div/div[5]/div/div[2]/div[2]/div[2]/table/tbody/tr/td[24]/button')
# //*[@id="tr_E9004F0B2BFA93B3E0531E7E640A774C"]/td[24]
time.sleep(2)
my.click()

input()
driver.close()
