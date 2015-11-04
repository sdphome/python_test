#!/usr/bin/env python
# -*-coding: utf-8 -*-
from selenium import webdriver
from time import sleep, time, strftime
from selenium.webdriver.common.keys import Keys
import os, sys, re
import unicodedata, datetime
import urllib, urllib2
from PIL import Image
from pytesseract import image_to_string
from BeautifulSoup import BeautifulSoup
from PyQt4 import QtCore, QtGui

global login_url, tender_url, username, password, paypasswd, browser, balance, total_interest, total_assets, myhome_url, rate, bid_time, started

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName(_fromUtf8("Form"))
        Form.resize(796, 543)
        self.frame = QtGui.QFrame(Form)
        self.frame.setGeometry(QtCore.QRect(0, 0, 801, 151))
        self.frame.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtGui.QFrame.Raised)
        self.frame.setObjectName(_fromUtf8("frame"))
        self.label = QtGui.QLabel(self.frame)
        self.label.setGeometry(QtCore.QRect(10, 10, 46, 13))
        self.label.setObjectName(_fromUtf8("label"))
        self.lineEdit = QtGui.QLineEdit(self.frame)
        self.lineEdit.setGeometry(QtCore.QRect(60, 10, 161, 20))
        self.lineEdit.setObjectName(_fromUtf8("lineEdit"))
        self.label_2 = QtGui.QLabel(self.frame)
        self.label_2.setGeometry(QtCore.QRect(10, 40, 46, 13))
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.label_3 = QtGui.QLabel(self.frame)
        self.label_3.setGeometry(QtCore.QRect(10, 70, 46, 13))
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.lineEdit_2 = QtGui.QLineEdit(self.frame)
        self.lineEdit_2.setGeometry(QtCore.QRect(60, 40, 161, 20))
        self.lineEdit_2.setObjectName(_fromUtf8("lineEdit_2"))
        self.lineEdit_3 = QtGui.QLineEdit(self.frame)
        self.lineEdit_3.setGeometry(QtCore.QRect(60, 70, 161, 20))
        self.lineEdit_3.setObjectName(_fromUtf8("lineEdit_3"))
        self.label_4 = QtGui.QLabel(self.frame)
        self.label_4.setGeometry(QtCore.QRect(300, 10, 46, 13))
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.label_5 = QtGui.QLabel(self.frame)
        self.label_5.setGeometry(QtCore.QRect(300, 40, 46, 13))
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.label_6 = QtGui.QLabel(self.frame)
        self.label_6.setGeometry(QtCore.QRect(300, 70, 46, 13))
        self.label_6.setObjectName(_fromUtf8("label_6"))
        self.lineEdit_4 = QtGui.QLineEdit(self.frame)
        self.lineEdit_4.setGeometry(QtCore.QRect(360, 10, 141, 20))
        self.lineEdit_4.setObjectName(_fromUtf8("lineEdit_4"))
        self.lineEdit_5 = QtGui.QLineEdit(self.frame)
        self.lineEdit_5.setGeometry(QtCore.QRect(360, 40, 141, 20))
        self.lineEdit_5.setObjectName(_fromUtf8("lineEdit_5"))
        self.lineEdit_6 = QtGui.QLineEdit(self.frame)
        self.lineEdit_6.setGeometry(QtCore.QRect(360, 70, 141, 20))
        self.lineEdit_6.setObjectName(_fromUtf8("lineEdit_6"))
        self.pushButton = QtGui.QPushButton(self.frame)
        self.pushButton.setGeometry(QtCore.QRect(600, 20, 75, 23))
        self.pushButton.setObjectName(_fromUtf8("pushButton"))
        self.textBrowser = QtGui.QTextBrowser(Form)
        self.textBrowser.setGeometry(QtCore.QRect(500, 180, 291, 361))
        self.textBrowser.setObjectName(_fromUtf8("textBrowser"))
        self.textBrowser_2 = QtGui.QTextBrowser(Form)
        self.textBrowser_2.setGeometry(QtCore.QRect(0, 180, 491, 361))
        self.textBrowser_2.setObjectName(_fromUtf8("textBrowser_2"))
        self.label_7 = QtGui.QLabel(Form)
        self.label_7.setGeometry(QtCore.QRect(10, 160, 46, 13))
        self.label_7.setObjectName(_fromUtf8("label_7"))
        self.label_8 = QtGui.QLabel(Form)
        self.label_8.setGeometry(QtCore.QRect(500, 160, 46, 13))
        self.label_8.setObjectName(_fromUtf8("label_8"))

        self.retranslateUi(Form)
        QtCore.QObject.connect(self.pushButton, QtCore.SIGNAL(_fromUtf8("clicked()")), self.clickBegin)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def clickBegin(self):
        global username, password, paypasswd, rate, bid_time, started
        if started == 0:
            started = 1
        else:
            started = 0
            print("exit")
            return
        username = str(self.lineEdit.text())
        password = str(self.lineEdit_2.text())
        paypasswd = str(self.lineEdit_3.text())
        bid_time = int(self.lineEdit_5.text())
        rate = int(self.lineEdit_6.text())
        if username == "" or password == "" or paypasswd == "":
            print("username=[%s]; password=[%s];paypassword=[%s]" %(username, password, paypasswd))
            return
        elif bid_time == 0 or rate == 0:
            bid_time = 12
            rate = 18
        print("username=[%s]; password=[%s];paypassword=[%s], bid_time=[%d]; rate=[%d]." %(username, password, paypasswd, bid_time, rate))

    def retranslateUi(self, Form):
        Form.setWindowTitle(_translate("Form", "Form", None))
        self.label.setText(_translate("Form", "用户名", None))
        self.label_2.setText(_translate("Form", "登录密码", None))
        self.label_3.setText(_translate("Form", "支付密码", None))
        self.label_4.setText(_translate("Form", "可用余额", None))
        self.label_5.setText(_translate("Form", "月数(<=)", None))
        self.label_6.setText(_translate("Form", "利率(>=)", None))
        self.pushButton.setText(_translate("Form", "开始投标", None))
        self.label_7.setText(_translate("Form", "扫描详情", None))
        self.label_8.setText(_translate("Form", "成功详情", None))



"""
need put chromedriver.exe path into PATH
1. PySide for UI
2. selenium for website operation
3. BeautifulSoup for parse html
"""

def init_global():
    global login_url, tender_url, username, password, paypasswd, browser, balance, total_interest, total_assets, started
    login_url = "https://passport.eloancn.com/login?service=http%3A%2F%2Fwww.eloancn.com%2Fpage%2FuserMgr%2FmyHome.jsp%3Furl%3Dfresh%2FuserDefaultMessage.action%26menuid%3D1%26timestamp%3D14447502342114579"
    tender_url = "http://www.eloancn.com/new/loadAllTender.action"
    myhome_url = "http://www.eloancn.com/page/userMgr/myHome.jsp"
    username = "15251611350"
    password = "xuyihua3590321"
    paypasswd = "xuyihua3590321"
    balance = 0
    total_interest = 0
    total_assets = 0
    rate = 0
    bid_time = 0
    started = 0

def cur_file_dir():
    path = sys.path[0]
    if os.path.isdir(path):
        return path
    elif os.path.isfile(path):
        return os.path.dirname(path)

def open_chrome():
    global browser
    browser = webdriver.Chrome()
    browser.maximize_window()


def login_eloance():
    global browser, login_url, username, password
    print("login website!")
    # auto login
    try:
        browser.set_page_load_timeout(5)
        browser.get(login_url)
        browser.execute_script('window.stop()')
    except:
        # TODO : check if enter successful
        pass

    print("Enter username and password")
    browser.find_element_by_id("loginName").send_keys([username, Keys.TAB, password, Keys.ENTER])
    sleep(2)

    #cookie= browser.get_cookies()
    #print cookie

    print("login successful!!!")

def goto_myhome():
    global myhome_url
    try:
        browser.set_page_load_timeout(5)
        browser.get(myhome_url)
        browser.execute_script('window.stop()')
    except:
        # TODO : check if enter successful
        pass

def unicode_to_int(u_data):
    temp1 = u_data.split('.')
    temp2 = temp1[0]    #just keep integer
    temp3 = unicodedata.normalize('NFKD', temp2).encode('ascii','ignore')
    temp4 = temp3.replace(',', '')
    return int(temp4)

def get_balance():
    global balance, browser
    webdata = browser.find_element_by_id("statField2").text
    balance = unicode_to_int(webdata)
    print("userful balance is %d元" %balance)
    return balance

def get_total_interest():
    global total_interest, browser
    webdata = browser.find_element_by_id("accumulative").text
    total_interest = unicode_to_int(webdata)
    print("total interest is %d元" %total_interest) 

def get_total_assets():
    global total_interest, browser
    webdata = browser.find_element_by_id("total_assets").text
    total_assets = unicode_to_int(webdata)
    print("total assets is %d元" %total_assets)

def get_money():
    get_balance()
    get_total_interest()
    get_total_assets()

def load_tend_web():
    global tender_url, browser
    # load tender website
    try:
        browser.set_page_load_timeout(1)
        browser.get(tender_url)
        browser.execute_script('window.stop()')
    except:
        # TODO : check if enter successful
        #print("load_tend_web except")
        pass

def crop_verify_code(code_name):
    global browser
    pay_name = "pay.png"
    browser.save_screenshot(pay_name)
    #crop the verify code image
    im = Image.open(pay_name)
    box = (870, 410, 922, 425)
    region = im.crop(box)
    region.save(code_name)

def get_verify_code():
    threshold = 140
    code_name = "code.png"
    table = []

    # get verify code picture
    crop_verify_code(code_name)

    for i in range(256):
        if i < threshold:
            table.append(0)
        else:
            table.append(1)

    rep = {'O':'0',
           'I':'1','L':'1',
           'Z':'2',
           'S':'8'
           };
    im = Image.open(code_name)
    imgry = im.convert('L')
    #imgry.save('g'+code_name)

    out = imgry.point(table, '1')
    #out.save('b' + code_name)

    text = image_to_string(out)

    text = text.strip()
    text = text.upper()

    for r in rep:
        text = text.replace(r, rep[r])
    print(text)
    return text

def auto_bid():
    global browser, paypasswd
    load_tend_web()
    # reload data
    lendtable = parse_lendtable()
    lendtable = sort_lendtable(lendtable)
    if lendtable == []:
        return

    max_rest_no = lendtable[0]['no']
    xpath_id = 5 * max_rest_no
    xpath = "/html/body/div[8]/div[2]/div[4]/dl/dd[" + str(xpath_id) + "]/a"
    #browser.save_screenshot("before.png")
    browser.find_element_by_xpath(xpath).click()
    sleep(1)
    #browser.save_screenshot("click.png")
    # TODO: input money
    # click 'auto input'
    browser.find_element_by_xpath("//*[@id=\"fastLender_1\"]/div[2]/div/p[2]/a").click()
    # input pay password
    browser.find_element_by_xpath("//*[@id=\"paypassowrd\"]").send_keys(paypasswd)
    #browser.save_screenshot("enter_paypass.png")
    while True:
    # get and input verify code
        verify_code = get_verify_code()
        browser.find_element_by_xpath("//*[@id=\"tenderRecordRandCode\"]").send_keys(verify_code)
        browser.save_screenshot("before_bid.png")
        # make sure bid
        browser.find_element_by_xpath("//*[@id=\"fastLender_1\"]/div[2]/div/p[6]/input[2]").click()
        browser.save_screenshot("finish_bid.png")
        if verify_code != "":
            break

def parse_lend_time(tag):
    time_str = str(tag.contents[1].contents[0])
    time = (time_str.split('>')[1]).split('<')[0]
    return int(time)

def parse_lend_schedule(tag):
    schedule_str = str(tag.contents[1].contents[0].contents[0])
    schedule = (schedule_str.split('%')[1]).split('>')[1]
    # just get integer
    schedule = schedule.split('.')[0]
    return int(schedule)

def parse_other(tag):
    money_str = str(tag.contents[1].contents[0])
    tender_id_tag = tag.contents[3].contents[1]
    rate_str = str(tender_id_tag.contents[0])
    tender_id = (str(tender_id_tag)).split('_')[1]
    #tender_id = int(tender_id_str.split('_')[1])
    money = int(money_str[3:].replace(',', ''))
    rate = int(rate_str[0:2])
    other = [money, rate, tender_id]
    return other


"""
1. get >=18% bid
2. sort bid money
3. check if balance > max bid money
4. get avaliable id to invest

## condiction:class="lendtable"/tenderid/
## each bid have 4 items
## id: needAmount_189691
need return a list:{[tenderid, time, rate, schedule], [...]}
"""

def parse_lendtable():
    global tender_url
    table = [] # new array
    lend_page = ""
    while started:
        try:
            lend_page = urllib2.urlopen(tender_url).read()
        except:
            lend_page = ""
            print("Internal Server Error")
            continue
        break

    if lend_page != "":
        soup = BeautifulSoup(''.join(lend_page))
        lendtable = soup.findAll(attrs={'class' : re.compile("lendtable")})  # get all lendtable, type:BeautifulSoup.ResultSet
        c1_child = lendtable[0]         # 1
        c2_child = c1_child.contents[1] # 2

        # TODO: if 100%, break
        # begin dividing:
        i = 0
        j = 0       
        dic = {}
        for c3_child in c2_child:
            i = i + 1

            """
            i == 2:  lender pic, useless
            i == 4:  title and lender name, useless
            i == 6:  lend money, tender_id and interest rate(very useful) *****
            i == 8:  lend time, useful   **
            i == 10: schedule, useful(first check)    ***
            i == 12: count, useless
            """
            if i == 8:
                # now time is useless, ignore it.
                #time = parse_lend_time(c3_child)
                #dic['time'] = time
                pass
            elif i == 10:
                schedule = parse_lend_schedule(c3_child)
                dic['schedule'] = schedule
                # in case schedule is noninteger, so -1
                dic['rest'] = dic['money']/100*(100-dic['schedule']-1)
            elif i == 6:
                other = parse_other(c3_child)
                dic['tender_id'] = other.pop()
                dic['rate'] = other.pop()
                dic['money'] = other.pop()
            if i % 12 == 0:
                i = 0;
                j = j + 1
                dic['no'] = j
                # filter table
                if dic['rest'] <= 0 or dic['rate'] < rate:
                    #print("Drop this bid, schedule=%d, rate=%d." %(dic['schedule'], dic['rate']))
                    pass
                else:
                    print dic
                    table.append(dic)
                dic = {}    # new dictionary

    return table

def sort_lendtable(table):
    #table.sort(lambda x, y:cmp(x['rest'], y['rest']))
    table = sorted(table, key=lambda x:x['rest'], reverse=True)
    return table

def start():
    global started
    open_chrome()
    login_eloance()
    #get_money()

    while started:
        times = 1
        while started:
            lendtable = parse_lendtable()
            lendtable = sort_lendtable(lendtable)

            if lendtable == []:
                #print("%s --- check %d times." %(str(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")), times))
                times = times + 1
                if times % 400 == 0:
                    load_tend_web()
            else:
                #for dic in lendtable:
                #    print dic
                break

        auto_bid()
        goto_myhome()
        balance = get_balance()
        if balance < 100:
            print("now balance is %d元." %balance)
            break

    print("End")
    global browser
    browser.quit()

def end():
    global browser
    browser.quit()

def main():
    global started
    init_global()
    app = QtGui.QApplication(sys.argv)
    Form = QtGui.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    #while True:
    #    sleep(2)
    #    if started ==1:
    #        start()
    sys.exit(app.exec_())

# main function
if __name__ == '__main__':
    main()

