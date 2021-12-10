#!/usr/bin/env python


__description__ = "This program uses Selenium WebDriver to Access Poliformat®"

import selenium
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager
import loading as ld
from selenium import webdriver
import threading
import pickle
import os.path
from getpass import getpass





# Config

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)
chrome_options.add_argument("--incognito")
global browser

# Info

__author__ = "Dairon Andrés Benites Aldaz"
__copyright__ = "Copyright 2021, @daibeal"
__credits__ = "Polytechnic University of Valencia"
__license__ = "GPL"
__version__ = "1.0.1"
__maintainer__ = "@daibeal"
__email__ = "contact@andresbenites.es"
__status__ = "Production"
__main__info = [__author__, __copyright__, __credits__, __license__, __version__, __maintainer__, __email__, __status__]
print('\n'.join(__main__info))



#load data
is_previous__data__available = os.path.isfile('./login.data')
if(is_previous__data__available):
    inputFile = 'login.data'
    fd = open(inputFile, 'rb')
    dataset = pickle.load(fd)
else:
    # Terminal input
    uss__In = input("\nEnter your username - [DNI/NIE]: ")
    pass__In = getpass("Enter your password: ")
    # Check Store
    accept = input('Do you want to save your login info? [Y/N]').lower()
    if(accept=="y"):
        dataset = [uss__In,pass__In]
        outputFile = 'login.data'
        fw = open(outputFile, 'wb')
        pickle.dump(dataset, fw)
        fw.close()






# User info
if(is_previous__data__available):
    user_name = dataset[0]
    password = dataset[1]
else:
    user_name = uss__In
    password = pass__In


def loading():

    ld.print_bar()


def nav_browser():
    # Init
    browser = webdriver.Chrome(ChromeDriverManager().install())
    # HTML selectors and Ids
    box__1 = 'dni'
    box__2 = 'clau'
    label__1 = '/html/body/div/div[1]/div[4]/div[4]/div[1]/div[1]/div[1]/div[4]/a[2]'

    # URL
    url = 'https://intranet.upv.es/pls/soalu/est_intranet.ni_portal_n?P_IDIOMA=i'

    # Access to the webpage

    browser.get(url)

    # First Window

    try:
        browser.find_element_by_name(box__1).send_keys(user_name)
        browser.find_element_by_name(box__2).send_keys(password)
        browser.find_element_by_name(box__2).send_keys(Keys.ENTER)

        # Second Window

        browser.find_element_by_xpath(label__1).click()
        success(browser)
    except selenium.common.exceptions.NoSuchElementException as ex:
        print('Error code: 001 - ' + ex)


def success(browser):
    print('Everything all right!')
    user_name = browser.find_element_by_class_name('Mrphs-userNav__submenuitem--username').text
    print('Welcome, ' + user_name + "!")
    while (True):
        pass


# Create two threads as follows
try:
    t1 = threading.Thread(target=loading)
    t2 = threading.Thread(target=nav_browser)
    t1.start()
    t2.start()    
except RuntimeError:
    print("Error: unable to start thread")

t1.join()
t2.join()


