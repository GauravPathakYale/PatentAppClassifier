from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import os
import urllib3

def initializeRemote(service,args=["--headless"]):
    capabilities = {'chrome.binary':'chromedriver.exe','chromeOptions':{"args":args}}
    browser = webdriver.Remote(service.service_url, capabilities)
    return  browser

def initialize(svc):
    path_to_chromedriver = 'chromedriver.exe'
    options = Options()
    #options.add_argument('--headless')
    browser = webdriver.Chrome(executable_path=path_to_chromedriver,chrome_options=options)
    return  browser

#def NavigateToCase(browser,docket):
    path = 'http://civilinquiry.jud.ct.gov/CaseDetail/PublicCaseDetail.aspx?DocketNo=' + docket
    browser.get(path)

def NavigateToCase(browser,docket):
    path = "file:///D:/Foreclosures/files/"+docket+".html"
    browser.get(path)

def getRows(browser):
    return browser.find_elements(By.XPATH,"//table[@id='ctl00_ContentPlaceHolder1_CaseDetailDocuments1_gvDocuments']/tbody/tr")

def checkInvalid(browser):
    message = browser.find_elements(By.XPATH,"//font[@color='red']")
    if message != []:
        if "is not found or is not electronically available" in message[0].text:
            return True
        elif "Please verify that the docket number was entered correctly" in message[0].text:
            return True
        elif "Invalid Docket Number" in message[0].text:
            return True
    else:
        return False

def close(browser):
    browser.quit()


def downloadFile(url):
    filedata = urllib3.urlopen(url)
    data = filedata.read()

    with open('test.pdf','wb') as f:
        f.write(data)



