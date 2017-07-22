#!/usr/bin/python3.4

import sys, re, HTMLInfo, genHTML, time, os

def process(url):
    start = time.time()
    info = HTMLInfo.HTMLinfo(url)
    info.shop()
    info.getGoods()
    info.replaceGoods()
    info.createURL()
    info.getItemList()
    info.multiProcess()       # multi threads (4)

    genHTML.createHTML(info.infolist)

    print("Done!")
    end = time.time()
    print("costs %0.2f seconds"%(end - start))

urlList = []

def getInfoFromurlLink():
    with open("cfg/urlLink", "r") as f:
         for line in f.readlines():
             url = re.sub('\n', '', line)
             if re.search('http', url) and not re.search('^#', url):
                 urlList.append(url)

getInfoFromurlLink()
genHTML.clearHTML()
if urlList:
    for i in urlList:
        try:
            process(i)
        except:
            print("Unexpected error:", sys.exc_info()[0])

driver = HTMLInfo.getWebdriver()
if driver:
    url = "file://" + os.getcwd() + "/show.html"
    driver.get(url)
    driver.maximize_window()

