#注意：在第一次填报时需要手动填写信息，之后才能使用该程序运行
#该程序以谷歌浏览器为例，其他浏览器类似
from selenium import webdriver as web 
from time import sleep
import threading
from selenium.webdriver.chrome.options import Options
def autoHealth(STUDENTID,PASSID):
    try:
        # chrome_options = Options()
        # chrome_options.add_argument("--headless")
        # chrome_options.add_argument("--disable-gpu")
        #更改您的驱动地址
        #bro = web.Chrome(executable_path=r"G:\chromedriver.exe",chrome_options=chrome_options)
        bro = web.Chrome(executable_path=r"G:\chromedriver.exe")
        url_login = "https://authserver.nuist.edu.cn/authserver/login?"
        try:
            bro.get(url = url_login)
            bro.find_element_by_css_selector("#username").send_keys(STUDENTID)
            bro.find_element_by_css_selector("#password").send_keys(PASSID)
            bro.find_element_by_css_selector("#login_submit").click()
        except Exception as e:
            print("用户登录失败，请重新登录！")
        # sleep(3)
        # url_index1 = "http://my.nuist.edu.cn/index.portal"
        # bro.get(url = url_index1)
        sleep(3)
        url_index2 = "http://e-office2.nuist.edu.cn/taskcenter/workflow/index"
        bro.get(url = url_index2)
        sleep(3)
        url_1 = "http://e-office2.nuist.edu.cn/infoplus/form/3958255/render"
        bro.get(url = url_1)
        sleep(3)
        bro.find_element_by_css_selector("input[name = 'fieldSTQKfrtw']").send_keys("36.5")
        sleep(2)
        bro.find_element_by_css_selector("input[name = 'fieldCNS']").click()
        sleep(2)
        bro.execute_script("$('nobr:contains(确认填报)').click()")
        bro.find_element_by_css_selector("button.dialog_button.default.fr").click()
        sleep(2)
        bro.find_element_by_css_selector("button.dialog_button.default.fr").click()
        sleep(2)
        print("健康信息填报成功！")
        sleep(5)
        bro.close()
    except Exception as e:
        print("健康信息填报失败！")
def repeat(id, key):
    autoHealth(id,key)
    # 60 * 60 * 24
    timer = threading.Timer(86400, repeat)
    timer.start()
if __name__=="__main__":
    #可以在此处填写您的学号和密码：
    id = input("请输入您的学号：")
    key = input("请输入您的密码：")
    repeat(id = id,key = key)