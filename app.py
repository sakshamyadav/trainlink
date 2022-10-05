import streamlit as st 
from splinter import Browser
import selenium
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import Select
import time
import datetime
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions as EC
import os 
from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from webdriver_manager.firefox import GeckoDriverManager


#get today's date
today = datetime.date.today()

def dest_switch(dest):
    if dest == 'mel':
        return 'Melbourne (Southern Cross) Station'
    elif dest == 'cbr':
        return 'Canberra (Kingston) Station'

def weekday(day):
    if day == "mon":
        return 0
    elif day == "tue":
        return 1
    elif day == "wed":
        return 2
    elif day == "thu":
        return 3
    elif day == "fri":
        return 4
    elif day == "sat":
        return 5
    elif day == "sun":
        return 6

#function to switch month to number
def calendar_mth(mth):
    if mth == "jan":
        return 1
    elif mth == "feb":
        return 2
    elif mth == "mar":
        return 3
    elif mth == "apr":
        return 4
    elif mth == "may":
        return 5
    elif mth == "jun":
        return 6
    elif mth == "jul":
        return 7
    elif mth == "aug":
        return 8
    elif mth == "sep":
        return 9
    elif mth == "oct":
        return 10
    elif mth == "nov":
        return 11
    elif mth == "dec":
        return 12 

travel_date = 'next fri'
return_date = 'next sat'
dest = 'mel'
travel_date = travel_date.split()
return_date = return_date.split()
dest = dest_switch(dest)

if len(travel_date) == 3:
    travel_day = int(travel_date[0])
    travel_mth = calendar_mth(travel_date[1]) 
    travel_yr = int(travel_date[2])

    travel_date = datetime.date(travel_yr,travel_mth,travel_day)

    days = travel_date - today 
    num_keys_travel = days.days

elif len(travel_date) == 2:
    if travel_date[0] == 'this':
        num_keys_travel = weekday(travel_date[1]) - today.weekday() 

    elif travel_date[0] == 'next':
        num_keys_travel = weekday(travel_date[1]) - today.weekday() + 7

##########
if len(return_date) == 3:
    travel_day = int(return_date[0])
    travel_mth = calendar_mth(return_date[1]) 
    travel_yr = int(return_date[2])

    return_date = datetime.date(travel_yr,travel_mth,travel_day)

    days = return_date - today 
    num_keys_return = days.days

elif len(return_date) == 2:
    if return_date[0] == 'this':
        num_keys_return = weekday(return_date[1]) - today.weekday() 

    elif return_date[0] == 'next':
        num_keys_return = weekday(return_date[1]) - today.weekday() + 7


firefoxOptions = Options()
firefoxOptions.add_argument("--headless")

driver = webdriver.Firefox(
    options=firefoxOptions,
    executable_path = GeckoDriverManager().install()
)



driver.get('https://transportnsw.info/regional-bookings/')


elem = driver.find_element(By.ID,'returnLabel').click();


elem = driver.find_element(By.XPATH,'//*[@id="tniFromStop"]').send_keys("Sydney (Central) Station");
elem = driver.find_element(By.XPATH,'//*[@id="tniToStop"]').send_keys(dest);

dropdown = Select(driver.find_element(By.ID,'tniPassengerConcessionType0'));
dropdown.select_by_visible_text("Premium 6 Month Discovery Pass");
print('fgfgfrt,',dropdown)

elem = driver.find_element(By.XPATH,'//*[@id="tniPassengerConcessionId0"]').send_keys("2022091251424");
elem = driver.find_element(By.XPATH,'//*[@id="tniPassengerConcessionFamilyName0"]').send_keys("Yadav");
print('dfffde,',elem)

elem = driver.find_element(By.XPATH,'//*[@id="tniDepartingDate"]').click();
print('asdfdfdas,',elem)
actions = ActionChains(driver)
actions.send_keys(Keys.ARROW_RIGHT * num_keys_travel)
actions.send_keys(Keys.RETURN)
actions.perform()

elem = driver.find_element(By.XPATH,'//*[@id="tniReturningDate"]').click();

actions = ActionChains(driver)
actions.send_keys(Keys.ARROW_RIGHT * num_keys_return)
actions.send_keys(Keys.RETURN)
actions.perform()
print('asdas,',elem)
elem = driver.find_element(By.XPATH,'//*[@id="tniSubmitButton"]').click();

elem = WebDriverWait(driver, 30).until(
        EC.presence_of_element_located((By.XPATH, "/html/body/app-root/app-offers/div/div/div[2]/app-itinerary-list/ul/app-itinerary[2]/li/a/app-itinerary-summary-header/article/div/div[1]")) #This is a dummy element
    )
elem.click()
print('dsfsdfd',elem)
browser.find_by_xpath('//*[@id="collapseOne"]/article/footer/app-itinerary-fares/div/fieldset/ul/li[2]/app-itinerary-fare-class/div/div[2]/div/div/label').click()
print('made it here',elem)

browser.find_by_xpath('//*[@id="collapseOne"]/article/footer/app-itinerary-fares/div/div[4]/button').click()
browser.find_by_xpath('/html/body/app-root/app-offers/div/div/div[2]/app-itinerary-list/ul/app-itinerary[2]/li/a/app-itinerary-summary-header/article/div/div[1]').click()
print('made it here too',elem)

browser.find_by_xpath('//*[@id="collapseOne"]/article/footer/app-itinerary-fares/div/fieldset/ul/li[2]/app-itinerary-fare-class/div/div[2]/div/div/label').click()
browser.find_by_xpath('//*[@id="collapseOne"]/article/footer/app-itinerary-fares/div/div[4]/button').click()
print('fine here as well',elem)

dropdown = Select(driver.find_element(By.ID,'genderSelect0'));
dropdown.select_by_visible_text("Male");
print('trrtwd',dropdown)

elem = driver.find_element(By.XPATH,'//*[@id="contactEmailInput"]').send_keys("sakshamyadav11@gmail.com");
elem = driver.find_element(By.XPATH,'//*[@id="contactPhoneInput"]').send_keys("0450513031");
elem = driver.find_element(By.ID,'i2').click();
print("CP2")
#wait 10 secs before clicking
time.sleep(10)
elem = driver.find_element(By.ID,'detailsConfirmationButton').click();
print("CP3")
driver.quit()
browser.quit()
print("CP1")


